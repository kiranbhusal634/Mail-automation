# Mail-automation
Sends personalized emails to multiple participants
📧 Automated Chess Tournament Email Sender — My Real-World Python Solution
Hi, I'm Kiran Bhusal, and this project comes straight from a real experience during my college life!

🎯 The Backstory
I was part of the organizing committee for a Chess Tournament at my college. One of my key responsibilities was to follow up with participants and share event details, tie sheets, and updates.

When the list grew to nearly 100 participants, manually sending emails became impractical. Rather than doing it one by one, I decided to automate the process using my Python skills and a little logic — getting the job done in seconds instead of hours!

This project is the exact tool I built and used to send those participant emails efficiently. Here’s how it works:

💡 What This Project Does
✔ Sends personalized emails to multiple participants 
✔ Uses secure Gmail SMTP service  
✔ Plain text emails for easy delivery (can be upgraded to HTML)  
✔ Automates bulk messaging in seconds 
✔ Real-world tested during my college chess tournament 

🛠️ Technologies Used
Python 3
smtplib for sending emails
email.mime for formatting messages
Gmail SMTP with TLS encryption

⚙️ Setup & How I Used It
Step 1: Clone the Repo
git clone https://github.com/kiranbhusal634/chess_tournament_email_sender.git
cd chess_tournament_email_sender

Step 2: Edit with Your Details
Open send_emails.py and update:

sender_email = "your_email@gmail.com"
sender_password = "your_app_password_here"

recipients = [
    "participant1@example.com",
    "participant2@example.com",
]

I used my Gmail App Password, keeping my account secure.
If you're trying this, set up an App Password.

Step 3: Run the Script
python send_emails.py
Done! In my case, nearly 100 participants got their invites and tie sheets instantly.

🚀 What I Learned
✅ How to automate repetitive tasks with Python
✅ Real-world application of smtplib and email handling
✅ Confidence boost seeing my small AI-inspired automation in action
✅ Saving hours of manual effort with a few lines of code


🌱 Possible Future Upgrades
Read recipient list from external .txt or .csv files
Add HTML email formatting
Personalize messages with names
Include attachments like PDFs or images
Build a GUI version for non-programmers

🤝 Want to Use or Improve It?
Feel free to fork this project, adapt it to your event, or suggest improvements. I’m always excited to see how small bits of code make a big difference.

✨ About Me
I'm Kiran Bhusal, a Python enthusiast passionate about practical projects, AI, and automation. This project is part of my journey to apply coding to real-world problems — and there’s more to come!

Thanks for checking out my project!
Want help using it for your event? Message me anytime.



