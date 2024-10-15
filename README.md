# Custom Avatar Generator

## Overview
The **Custom Avatar Generator** is a Python-based tool that allows users to create unique avatars by combining various graphical components such as backgrounds, faces, clothing, hair, facial hair, lips, accessories, and special features. This program utilises the Pillow library to manipulate and combine images.

## Features
- Customisable avatars using user-specified IDs for various components.
- Option to skip certain components by entering '0'.
- Supports multiple layers, allowing for complex and varied avatar designs.
- Outputs the final avatar as a PNG image file.

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.x
- Pillow library

You can install Pillow using pip:

```bash
pip install pillow
Directory Structure
Your project should have the following directory structure:

graphql
Copy code
/Custom Avatar Generator
│
├── Assets/
│   ├── Background/
│   ├── Face/
│   ├── Clothing/
│   ├── Hair/
│   ├── FacialHair/
│   ├── Lips/
│   ├── Accessories/
│   └── Special/
│
├── Output/           # Output folder for generated avatars
│
├── CustomAvatarGenerator.py           # Main script for generating avatars
│
└── LICENSE           # GNU General Public License

Usage
Run the Program: Execute the main.py script to start the avatar generation process:

bash
Copy code
python main.py
Input Component IDs: When prompted, enter the ID codes for each avatar component:

Background: ID code for background image.
Face: ID code for face image.
Clothing: ID code for clothing image.
Hair: ID code for hair image (specify colour, e.g., 1a) or enter 0 to skip.
Facial Hair: ID code for facial hair image (specify colour, e.g., 5e) or enter 0 to skip.
Lips: ID code for lips image or enter 0 to skip.
Accessories: ID code for accessories image or enter 0 to skip.
Special: ID code for special features image or enter 0 to skip.
View and Save Output: The program will display the generated avatar and save it in the Output directory with a filename based on the entered IDs.

Contribution
Contributions are welcome! If you have suggestions for improvements or features, please feel free to fork the repository and submit a pull request.

License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

Acknowledgements
This project uses the Pillow library for image processing.