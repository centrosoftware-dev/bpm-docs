using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.HttpOverrides;

var builder = WebApplication.CreateBuilder(args);

var users = builder.Configuration.GetSection("Users").Get<List<UserCredential>>() ?? new();

builder.Services
    .AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(options =>
    {
        options.LoginPath = "/login";
        options.LogoutPath = "/logout";
        options.ExpireTimeSpan = TimeSpan.FromHours(8);
        options.SlidingExpiration = true;
    });

var app = builder.Build();

// Azure App Service termina l'HTTPS a monte: senza questo, UseHttpsRedirection
// e il cookie "secure" vedrebbero ogni richiesta come HTTP.
app.UseForwardedHeaders(new ForwardedHeadersOptions
{
    ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
});

app.UseHttpsRedirection();
app.UseAuthentication();

app.MapGet("/login", (string? returnUrl, string? error) =>
    Results.Content(LoginPage.Render(returnUrl, error is not null), "text/html"));

app.MapPost("/login", async (HttpContext http, string? returnUrl) =>
{
    var form = await http.Request.ReadFormAsync();
    var username = form["username"].ToString();
    var password = form["password"].ToString();

    var user = users.FirstOrDefault(u =>
        string.Equals(u.Username, username, StringComparison.OrdinalIgnoreCase) &&
        u.Password == password);

    if (user is null)
    {
        var target = "/login?error=1" + (string.IsNullOrEmpty(returnUrl) ? "" : $"&returnUrl={Uri.EscapeDataString(returnUrl)}");
        return Results.Redirect(target);
    }

    var identity = new ClaimsIdentity(
        new[]
        {
            new Claim(ClaimTypes.Name, user.Username),
            new Claim(ClaimTypes.GivenName, user.EffectiveDisplayName)
        },
        CookieAuthenticationDefaults.AuthenticationScheme);

    await http.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme, new ClaimsPrincipal(identity));

    return Results.Redirect(string.IsNullOrEmpty(returnUrl) ? "/" : returnUrl);
});

app.MapGet("/logout", async (HttpContext http) =>
{
    await http.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
    return Results.Redirect("/login");
});

app.MapGet("/api/whoami", (HttpContext http) => Results.Json(new
{
    username = http.User.Identity?.Name,
    displayName = http.User.FindFirstValue(ClaimTypes.GivenName)
}));

// Da qui in poi, tutto (pagine, immagini, search_index.json, download) resta
// dietro login: nessuna eccezione oltre a /login e /logout.
app.Use(async (context, next) =>
{
    var path = context.Request.Path;
    if (path.StartsWithSegments("/login") || path.StartsWithSegments("/logout"))
    {
        await next();
        return;
    }

    if (context.User.Identity?.IsAuthenticated != true)
    {
        var returnUrl = Uri.EscapeDataString(context.Request.Path + context.Request.QueryString);
        context.Response.Redirect($"/login?returnUrl={returnUrl}");
        return;
    }

    await next();
});

app.UseStatusCodePagesWithReExecute("/404.html");
app.UseDefaultFiles();
app.UseStaticFiles();

app.Run();

record UserCredential
{
    public string Username { get; init; } = "";
    public string Password { get; init; } = "";
    public string? DisplayName { get; init; }

    public string EffectiveDisplayName => string.IsNullOrWhiteSpace(DisplayName) ? Username : DisplayName;
}

static class LoginPage
{
    public static string Render(string? returnUrl, bool showError)
    {
        var action = "/login?returnUrl=" + Uri.EscapeDataString(returnUrl ?? "/");
        var errorHtml = showError ? "<p class=\"error\">Utente o password non corretti.</p>" : "";

        return $$"""
        <!DOCTYPE html>
        <html lang="it">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Accesso - Documentazione BPM</title>
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #011e41;
                font-family: "Noto Sans", "Segoe UI", sans-serif;
            }
            form {
                background: #ffffff;
                color: #011e41;
                padding: 2.5rem;
                border-radius: 8px;
                width: 100%;
                max-width: 320px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
            }
            h1 {
                font-size: 1.3rem;
                margin: 0 0 1.5rem;
                border-bottom: 3px solid #17ff88;
                padding-bottom: 0.75rem;
            }
            label {
                display: block;
                font-size: 0.85rem;
                margin-bottom: 0.35rem;
            }
            input {
                width: 100%;
                padding: 0.5rem;
                margin-bottom: 1rem;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                font-size: 1rem;
            }
            button {
                width: 100%;
                padding: 0.6rem;
                background: #011e41;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                font-size: 1rem;
                cursor: pointer;
            }
            button:hover {
                background: #3093ef;
            }
            .error {
                color: #c0392b;
                font-size: 0.85rem;
                margin: -0.5rem 0 1rem;
            }
        </style>
        </head>
        <body>
        <form method="post" action="{{action}}">
            <h1>Documentazione BPM</h1>
            {{errorHtml}}
            <label for="username">Utente</label>
            <input id="username" name="username" autocomplete="username" required>
            <label for="password">Password</label>
            <input id="password" name="password" type="password" autocomplete="current-password" required>
            <button type="submit">Accedi</button>
        </form>
        </body>
        </html>
        """;
    }
}
