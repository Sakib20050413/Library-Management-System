Django Task: Library Management System

Objective
Combine your knowledge of Django models, views, URLs, and templates to build a simple
library management system.
Task Description
The end result of this project is a browser-based library catalog system where users can
interact with four core modules: Books, Authors, Members, and Borrowing records. By
the end of the project, the system will allow you to track the relationships between these
entities (e.g., which author wrote which book, and which member has borrowed which
book).Functional Workflow
The application follows a standard database-driven flow:
1. Catalog/List Pages:
○ When you navigate to a main list page (e.g., the Book Catalog), the app
queries the database and displays a collection of all items in that category.
○ This provides a high-level view of your library's inventory or member list.
2. Detail Pages :
○ Book Detail Page: When a user clicks on a specific book, the system
retrieves and displays in-depth information for that single record. Based on
your model requirements, this page would typically show the book's title, the
associated author, publication details, and its current status (e.g., "Available"
or "Borrowed").
○ Member Page: Similarly, clicking on a member displays their specific profile
information, which may include their contact details and a history of their
active or past borrowing transactions.
Key Functionalities
To meet the project requirements, your application must include these capabilities:
● Data Retrieval: The system provides both List Views (overview) and Detail Views
(specifics) for each of the four modules:
○ Books: View all books; view details for a specific book.
○ Authors: View all authors; view details/biography for a specific author.
○ Members: View all library members; view details for a specific member.
○ Borrowing: Manage the link between books and members (tracking who
checked out what).
● Data Relationship Management: A core part of the system is ensuring that the
"Borrowing" module correctly links a member to a specific book, and that the "Books"
module is correctly linked to an "Author."
● Testing and Validation: You will verify functionality by populating the database with
sample data to ensure that items can be linked, searched, and updated correctly.
Steps
1. Setup the Project and Apps
- If you haven't already, create a Django project (if you don't have one from the previous
task).
- Create four apps within your project:
1. Books
2. Authors
3. Members
4. Borrowing
2. Define the Models
Open each app's `models.py` and define the models.
3. Run Migrations
Create and apply the migrations for all apps:
4. Create Views
For each app, create a `views.py` with at least two views: a list view and a detail view.
Similarly, create views for authors, members, and borrowings.
5. Set Up URLs
- In each app's directory, create a `urls.py` file (if it doesn't exist) and define URL patterns
for your views.
6. Create Templates
7. Test the Application
8. Add Sample Data
- Use the Django shell to create sample data for testing:
Submission
Be ready to demonstrate your application and explain the relationships between models,
views, URLs, and templates.
