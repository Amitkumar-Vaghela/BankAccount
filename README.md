## Bank Management System

This repository contains a simple Bank Management System implemented in Python.
It consists of two classes: `bank` and `user`. 
The `bank` class is responsible for managing user registration data, 
while the `user` class provides functionality for user registration, login, and unregistering.


### Features:

- **User Registration**: Users can register with their name and phone number.
- **User Login**: Registered users can log in using their name and phone number.
- **User Unregister**: Users can unregister from the system.

### Usage:

1. **Register a User**:
   ```python
   obj = user()
   print(obj.register('Amit', 809069))

1 Login a User:   print(obj.login('Amit', 809069))
2 Unregister a User:  print(obj.unregister('Amit', 809069))

How to Contribute:
Fork the repository.
Clone the forked repository to your local machine.
Create a new branch for your feature (git checkout -b feature/YourFeatureName).
Make changes and commit them (git commit -am 'Add some feature').
Push the changes to your branch (git push origin feature/YourFeatureName).
Create a new Pull Request.

Navigate to the Project Directory:   cd bank-management-system

Run the Python Script:    python main.py

License
This project is licensed under the MIT License. See the LICENSE file for details.
















