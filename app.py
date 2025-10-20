"""
Flask web application for the Academic Mentorship Workflow.
Provides a web interface to run both OpenAI and Gemini workflows.
"""

import os
import json
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

# Import our workflow modules
from mentorship_workflow import run_workflow as run_openai_workflow
from gemini_mentorship_workflow import run_workflow as run_gemini_workflow

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

@app.route('/api/run-openai', methods=['POST'])
def run_openai():
    """Run the OpenAI workflow via API."""
    try:
        # Get form data
        user_input = request.form.get('user_input', '').strip()
        model = request.form.get('model', 'gpt-4o-mini')
        
        if not user_input:
            return jsonify({'error': 'User input is required'}), 400
        
        # Check if OpenAI API key is available
        if not os.getenv('OPENAI_API_KEY'):
            return jsonify({'error': 'OPENAI_API_KEY is not set. Please configure your OpenAI API key.'}), 400
        
        # Run the workflow
        result = run_openai_workflow(user_input)
        
        # Return the result
        return jsonify({
            'research_scope': result.get('research_scope', ''),
            'analyst_report': result.get('analyst_report', ''),
            'resource_map': result.get('resource_map', ''),
            'final_report': result.get('final_report', ''),
            'model_used': model
        })
        
    except Exception as e:
        app.logger.error(f"OpenAI workflow error: {str(e)}")
        return jsonify({'error': f'Workflow execution failed: {str(e)}'}), 500

@app.route('/api/run-gemini', methods=['POST'])
def run_gemini():
    """Run the Gemini workflow via API."""
    try:
        # Get form data
        user_input = request.form.get('user_input', '').strip()
        model = request.form.get('model', 'gemini-2.0-flash')
        
        if not user_input:
            return jsonify({'error': 'User input is required'}), 400
        
        # Check if Gemini API key is available
        if not os.getenv('GEMINI_API_KEY'):
            return jsonify({'error': 'GEMINI_API_KEY is not set. Please configure your Gemini API key.'}), 400
        
        # Run the workflow
        result = run_gemini_workflow(user_input)
        
        # Return the result
        return jsonify({
            'research_scope': result.get('research_scope', ''),
            'analyst_report': result.get('analyst_report', ''),
            'resource_map': result.get('resource_map', ''),
            'final_report': result.get('final_report', ''),
            'model_used': model
        })
        
    except Exception as e:
        app.logger.error(f"Gemini workflow error: {str(e)}")
        return jsonify({'error': f'Workflow execution failed: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    openai_available = bool(os.getenv('OPENAI_API_KEY'))
    gemini_available = bool(os.getenv('GEMINI_API_KEY'))
    
    return jsonify({
        'status': 'healthy',
        'openai_configured': openai_available,
        'gemini_configured': gemini_available,
        'workflows_available': {
            'openai': openai_available,
            'gemini': gemini_available
        }
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Load environment variables from .env file if it exists
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080, debug=True)
