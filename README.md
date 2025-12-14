# Flask Personal Website Template

A clean, modern, and responsive personal website template built with Flask. Perfect for showcasing your portfolio, projects, and professional information.

## Features

- 🎨 Modern and responsive design
- 📱 Mobile-friendly navigation
- 🏠 Home page with hero section
- 👤 About page with skills and experience
- 💼 Projects showcase page
- 📧 Contact form
- 🎯 Clean and maintainable code structure
- 🔧 Easy to customize

## Project Structure

```
qqss_personal/
├── app/
│   ├── __init__.py          # Application factory
│   ├── routes.py            # URL routes and views
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Stylesheet
│   │   ├── js/              # JavaScript files
│   │   └── images/          # Images
│   └── templates/
│       ├── base.html        # Base template
│       ├── home.html        # Home page
│       ├── about.html       # About page
│       ├── projects.html    # Projects page
│       └── contact.html     # Contact page
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/qqss88/qqss_personal.git
cd qqss_personal
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file for environment variables:
```bash
cp .env.example .env
```

## Usage

1. Run the development server:
```bash
python run.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Customization

### Update Personal Information

1. **About Page**: Edit `app/templates/about.html` to update your bio, skills, and experience
2. **Projects**: Modify the `projects_list` in `app/routes.py` to showcase your own projects
3. **Contact Info**: Update contact details in `app/templates/contact.html`
4. **Social Links**: Edit footer links in `app/templates/base.html`

### Styling

- All styles are in `app/static/css/style.css`
- Colors can be easily changed by modifying CSS variables in `:root`
- The design is fully responsive and mobile-friendly

### Adding New Pages

1. Create a new route in `app/routes.py`:
```python
@bp.route('/newpage')
def newpage():
    return render_template('newpage.html', title='New Page')
```

2. Create the template in `app/templates/newpage.html`
3. Add navigation link in `app/templates/base.html`

## Deployment

### Heroku

1. Create a `Procfile`:
```
web: python run.py
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Other Platforms

This Flask app can be deployed to various platforms including:
- AWS Elastic Beanstalk
- Google Cloud Platform
- DigitalOcean
- PythonAnywhere

## Security Notes

- Remember to change the `SECRET_KEY` in production
- Set `FLASK_DEBUG=False` in production
- Use environment variables for sensitive information

## Contributing

Feel free to fork this project and customize it for your own use. Pull requests are welcome!

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please open an issue on GitHub.
