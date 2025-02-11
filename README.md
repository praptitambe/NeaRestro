# NeaRestro

## Overview

NeaRestro is a web application designed to help users discover restaurants in their city based on their preferred cuisine. The platform aims to provide a seamless and user-friendly experience for food enthusiasts looking to explore new dining options. 

[Live View](https://nearestro-0ab3008aa139.herokuapp.com/)

## Responsive
NeaRestro is fully responsive, ensuring a seamless experience across various devices, including desktops, tablets, and mobile phones. 
The design adapts to different screen sizes, providing an optimal viewing experience whether you're at home or on the go.
![Am I Responsive](static/images/readme/responsive.png)

### Purpose

The primary purpose of NeaRestro is to connect users with a variety of restaurants in their city, categorized by different cuisines. Whether you are craving Italian, Chinese, Indian, or any other type of cuisine, NeaRestro makes it easy to find the perfect restaurant to satisfy your taste buds. Additionally, NeaRestro provides comments and rating-based suggestions, allowing users to make informed decisions based on the experiences and feedback of other diners.

### Problem It Solves

Finding a restaurant that serves your favorite cuisine can be a daunting task, especially in a large city with numerous dining options. NeaRestro addresses this problem by providing a centralized platform where users can search for restaurants based on cuisine type, location, and other relevant criteria. This eliminates the need for users to browse through multiple websites or rely on word-of-mouth recommendations. Additionally, NeaRestro includes user-generated comments and ratings, offering valuable insights and suggestions to help users choose the best restaurants based on the experiences of others.

### Value to Users

- **Convenience**: Users can quickly and easily find restaurants that match their culinary preferences without having to sift through unrelated options.
- **Variety**: NeaRestro offers a diverse range of cuisines, ensuring that users can find something to suit their tastes, no matter how specific.
- **User Reviews and Ratings**: The platform includes user-generated reviews and ratings, helping users make informed decisions based on the experiences of others. Users can read comments and see ratings for each restaurant, providing valuable insights into the quality of food and service.
- **Informed Choices**: By considering the comments and ratings of other users, individuals can make better-informed decisions when choosing a restaurant, ensuring a more satisfying dining experience.
- **User Interaction**: Users can add, delete, or update their own comments, allowing them to share their experiences and feedback with the community.
- **Detailed Information**: Each restaurant listing includes essential details such as address, contact information, and a brief description, making it easy for users to plan their visit.

NeaRestro is the go-to platform for anyone looking to explore the culinary landscape of their city, offering a comprehensive and enjoyable experience for food lovers everywhere.

#### MoSCoW Tecnhique
The MoSCoW technique is a prioritization method used to decide which features to implement in a project. It stands for:

- **Must-Have**: These are the essential features that the project cannot do without. They are critical for the application's functionality and must be included in the initial release.
- **Should-Have**: These features are important but not critical. They add significant value to the project and should be included if possible, but the project can still function without them.
- **Could-Have**: These are desirable features that can enhance the user experience but are not essential. They can be considered for future updates if time and resources permit.
- **Won't-Have**: These features are the least critical and will not be included in the current project scope. They may be revisited in future iterations.

By using the MoSCoW technique, I was able to focus on delivering the most critical features first, ensuring a functional and valuable application for users while planning for future enhancements.
I have implemented all Must-have and Should-have features. Could-have are for future implementations.

![MoSCoW Technique](static/images/readme/moscow.png)

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects kanban board](https://github.com/users/praptitambe/projects/11/views/1)
## Design

### Wireframes

The wireframes for NeaRestro were created using Balsamiq to create clear, visual layouts of the site's design. While the initial designs provided a solid foundation, some elements evolved during development to enhance the overall user experience. These changes, though different from the original wireframes, resulted in a more polished and user-friendly application.

- [Click here for desktop wireframe](static/images/readme/wireframe-desktop.png)
- [Click here for tablet wireframe](static/images/readme/wireframe-tablet.png)
- [Click here for mobile wireframe](static/images/readme/wireframe-mobile.png)

### Logo
The logo for NeaRestro was created by me, reflecting the essence of the application. Here are some key points about the logo:

- **Design Concept**: The logo combines elements of cutlery to visually represent the application's focus on food.
- **Color Scheme**: The colors used in the logo align with the overall color palette of the application, ensuring a cohesive visual identity.
- **Typography**: The font used in the logo is clean and modern, making it easily readable and visually appealing.
- **Scalability**: The logo is designed to be scalable, ensuring it looks great on various devices and screen sizes, from mobile phones to desktops.

- [logo](static/images/logo.png)

### Color Palette
![palette](static/images/readme/color.png)
- [Color Palette](https://colorhunt.co/palette/3d5300abba7cffe31af09319)

- #FFE31A - Navigation and footer background.
- #3D5300 - Background of cards and forms.
- #F09319 - Button color, text color on login,logout and signup form.
- #ABBA7C - Button color when hovered.
- #F5F2F2 - Text color.

### Typography 

![font style](static/images/readme/fonts.png)
[Google fonts](https://fonts.google.com/selection)
 - Heading -  'Playfair Display', serif
 - Body - 'Merienda', serif


## Key Features

- **Restaurant Search by Cuisine and Location**: Users can search for restaurants based on their preferred cuisine and location. This feature allows users to quickly find restaurants that match their culinary preferences.

- **User Reviews and Ratings**: Users can read reviews and ratings left by other diners. This feature helps users make informed decisions based on the experiences of others.

- **Add, Delete, and Update Comments**: Authenticated users can add, delete, and update their own comments on restaurant listings. This feature allows users to share their dining experiences and provide feedback.

- **Detailed Restaurant Information**: Each restaurant listing includes essential details such as address, contact information, cuisine type, a brief description, comments and average rating based on number of reviews. This feature provides users with all the necessary information to plan their visit.

- **Responsive Design**: The platform is designed to be responsive, ensuring a seamless user experience across different devices, including desktops, tablets, and mobile phones.

- **User Authentication**: Users can create accounts, log in, and manage their profiles. This feature ensures that only authenticated users can add, delete, or update comments.

- **Admin Panel**: An admin panel is available for managing restaurant listings, user comments, and other administrative tasks. This feature allows administrators to maintain the quality and accuracy of the information on the platform.

- **Search Restaurants**: When users input city or restaurant name in search bar with optional cousine type, the platform filtes restro suggestions based on the input. This feature helps users quickly find the restaurants they are looking for.

- **Accessibility Features**: The platform includes accessibility features such as high contrast mode, screen reader support, and keyboard navigation to ensure that it is usable by all users, including those with disabilities.

- **Social Media Integration**: Users can follow the platform on social media and share restaurant listings with their friends. This feature helps increase engagement and reach.

NeaRestro is designed to provide a comprehensive and enjoyable experience for food lovers, making it easy to discover and explore the culinary landscape of their city.

## Deployment
- **Platform:** [Platform used, e.g., Heroku, AWS, etc.]
- **High-Level Deployment Steps:** 
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
- **Verification and Validation:**
  - Steps taken to verify the deployed version matches the development version in functionality.
  - [Include any additional checks to ensure accessibility of the deployed application.]
- **Security Measures:**
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.

## AI Implementation and Orchestration

### Use Cases and Reflections:
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing: (If undertaken)**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
## Testing
- Please see [TESTING.md](TESTING.md) file for all testing.

- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing: (If undertaken)**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]

## Future Enhancements
- [List potential improvements or additional features for future development.]
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.