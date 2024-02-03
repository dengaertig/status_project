Website Status Page

This project provides a simple and elegant status page for monitoring the availability of websites. It allows users to add, delete, and view websites, along with their real-time online or offline status. Perfect for Web Developer who needs to know the Status of their Websites.

![cxcxyy](https://github.com/KenKoLegend/status_project/assets/50487808/595d81cf-5ca9-4c50-9b4f-f25eb182ea55)


Features
Website Monitoring: The status page checks the availability of added websites in real-time using ping.
User Interaction: 
Users can dynamically add new websites to monitor and remove existing ones.

Live Status Updates: 
The page dynamically updates the online or offline status of each website.

Bootstrap Styling: 
The user interface is enhanced using Bootstrap, providing a clean and responsive design.
Convenient Management: Websites can be added or deleted directly from the web interface without the need for an admin section.
Usage

![cxxay](https://github.com/KenKoLegend/status_project/assets/50487808/94269ec8-201f-4b2d-8ac1-5c0a15f8bcb7)


Clone the repository:

```
git clone git@github.com:KenKoLegend/status_project.git
```

Create a virtual environment and install dependencies:

```
cd status_project
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
pip install -r requirements.txt
```

Apply migrations and start the server:

```
python manage.py migrate
python manage.py runserver
```
Open the browser and navigate to http://localhost:8000/ to access the status page.

Customization
Styling: Customize the appearance of the status page by modifying the styles.css file in the static/css directory.
JavaScript Logic: Adapt the real-time status update logic in the status.js file located in the static/js directory.
Feel free to contribute, report issues, or suggest enhancements!

