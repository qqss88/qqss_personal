from flask import Blueprint, render_template, request, flash, redirect, url_for
from markupsafe import escape

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    """Home page route"""
    return render_template('home.html', title='Home')

@bp.route('/about')
def about():
    """About page route"""
    return render_template('about.html', title='About Me')

@bp.route('/projects')
def projects():
    """Projects page route"""
    projects_list = [
        {
            'title': 'Project One',
            'description': 'A sample project showcasing your work',
            'technologies': ['Python', 'Flask', 'HTML/CSS'],
            'link': '#'
        },
        {
            'title': 'Project Two',
            'description': 'Another interesting project',
            'technologies': ['JavaScript', 'React', 'Node.js'],
            'link': '#'
        },
        {
            'title': 'Project Three',
            'description': 'Your latest accomplishment',
            'technologies': ['Python', 'Django', 'PostgreSQL'],
            'link': '#'
        }
    ]
    return render_template('projects.html', title='Projects', projects=projects_list)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route
    
    Note: For production use, consider adding:
    - Flask-WTF for CSRF protection
    - Email validation library for robust email checking
    - Email sending functionality (e.g., Flask-Mail)
    """
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            flash('All fields are required.', 'error')
            return redirect(url_for('main.contact'))
        
        if len(name) > 100 or len(email) > 100 or len(message) > 1000:
            flash('Input exceeds maximum length.', 'error')
            return redirect(url_for('main.contact'))
        
        # In a real application, you would send an email or store this data
        # Escape user input to prevent XSS (rendered with | safe filter in template to avoid double-escaping)
        safe_name = escape(name)
        flash(f'Thank you for your message, {safe_name}! I will get back to you soon.', 'success')
        return redirect(url_for('main.contact'))
    
    return render_template('contact.html', title='Contact')
