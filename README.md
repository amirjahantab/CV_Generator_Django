**CV Generator**

This is a Django web application that allows users to submit their details and generate a downloadable CV (resume) in PDF format.

**Getting Started**

  
1. **Clone the repository:**
   ```bash
   git clone https://github.com/amirjahantab/CV_Generator_Django.git
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### URLs

- **admin/**: Django admin panel for managing profiles.
- **/**: Accepts user input to generate a CV.
- **<int:id>/**: Generates and downloads a CV based on the provided profile ID.
- **list/**: Displays a list of all CV profiles stored in the database.

### Templates

- **accept.html**: Form for users to fill out their details.
- **list.html**: Displays a list of CV profiles.
- **resume.html**: Template for generating CVs based on user profiles.

### Views

- **accept**: View function for accepting user input and saving it to the database.
- **resume**: View function for generating and downloading a CV based on the provided profile ID.
- **list**: View function for displaying a list of all CV profiles stored in the database.

**Features**

* Users can submit their details through a web form.
* Submitted details are stored in the database.
* Users can view a list of all saved CVs.
* Users can download a PDF of a specific CV.


* Consider using a CSS framework like Bootstrap for better responsiveness and styling.

I hope this helps!
