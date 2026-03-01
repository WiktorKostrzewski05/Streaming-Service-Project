# Watchy

A Django web app for a streaming service: browse movies and shows, subscribe, rate and review, and get recommendations. Built as a 3-person college 2nd year project.

## What it does
- **Home** — Landing page for the service.
- **Media** — Browse all content. Open a title to see details, trailer, and episodes/seasons.
- **Player** — Play media in a built-in player.
- **Staff tools** — Staff can add, edit, and delete content and media files.
- **Search** — Find movies and shows by keyword (title or description).
- **Subscriptions** — Stripe integration. Subscription status is checked for logged-in users.
- **Ratings & reviews** — Rate and review content. Invalid reviews are hidden on content pages.
- **Recommendations** — Suggestions based on favourite genre and watch history.
- **Watch progress** — Profile tracks watched media and completion time for recommendations.
- **Support** — Submit support tickets and view open/closed requests.
- **Users** — Sign up, view profile, and edit profile
- **Admin** — Django admin (and AdminPlus) for managing data and analysing subscription stats/top-rated content.

## Stack
- Python 3.11
- Django 4.2
- PostgreSQL
- Supabase
- Stripe
- Bootstrap 5
- django-crispy-forms
- Pillow
- Matplotlib
- Django Test Framework
- Vercel for deployment