# BraveHeartsTogether

To see the site [click here](https://bravehearts.onrender.com/)

BraveHeartsTogether is a site that aims to help veterans by providing a space where they can write and share their stories and experiences. It allows them to connect with other veterans and feel understood and supported. By sharing their stories, veterans can also help others better understand the challenges they face and raise awareness about veteran mental health. BraveHeartsTogether is a valuable tool to help veterans better manage their mental health and connect with a community of like-minded people.

![Mockup](media/images/mockup.png)

## User Experience (UX)

-   ### User stories

    -   #### User Goals

        1. As a User, I can access stories easily through the homepage and navigation bar.
        2. As a User, I can learn about the benefits of the website and its purpose on the homepage.
        3. As a User, I can easily access social media links so that I can interact with the website.
        4. As a User, I can find out more about the site by clicking on the about page.

    -   #### New User Goals

        1. As a New User, I can click on register and fill out a form to create an account.
        2. As a New User, I can choose to create a public profile or an anonymous profile.
        3. As a New User, I can start to write a story right away after the completion of my profile.
        
        
    -   #### Returning User Goals

        1. As a Returning User, I can login to write stories.
        2. As a Returning User, I can login to my profile and edit details and/or my profile picture.


-   ### Design
    -   #### Colour Scheme
        -   The main colours used are orange, gold, amber
    -   #### Logo
        -   The logo was designed to represent ...
    -   #### Favicon
        -   The Favicon is ...
    -   #### Typography
        -   The  google merriweather font is the main font used throughout the whole website.
    -   #### Imagery
        -   Imagery is important. The hero image is designed to be peaceful and relaxing and to encourage people to interact with the site.


## Features 

The site offers many features. Visiting users can easily read stories and blog articles via the responsive navigation bar at the top of the homepage. Recent blog posts and stories are also showcased on the homepage to help users easily discover new content and inspire them to share. Users can create either a public profile or an anonymous account to write and share stories. The profile provides CRUD functionality, allowing users to update their personal details. To create stories, users simply need to click on the "write a story" button, which is accessible on the homepage and the profile page. The site owner is responsible for creating the blog content. Additionally, the site has an "about" section that explains the site's purpose.

### Existing Features

- __Navigation Bar__

  - Featured on all pages, the full responsive navigation bar includes links to the Logo, Homepage, stories, blog and account and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

- __The landing page image__

  - The landing includes an image with text overlay of the website's title. 
  - This section introduces the user to BraveHeartsTogether with a beautiful colour palette to grab the user's attention.

- __Ethos Section__

  - The ethos section allows the user to see the benefits of joining BraveHeartsTogether, as well as the benefits of joining a community and sharing with others overall. 
  - This allows the user to see the value of creating an account and be encouraged to consider writing their own stories. 

- __Recent posts__

  - Viewing recent posts on the homepage will allow the user to see exactly what the site is about and help users easily discover new content and inspire them to write. 
  - This section will be automatically updated as new posts are created. 

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for BraveHeartsTogether. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media.

- __Account registration__

  - This page will allow the user to create an account with BraveHeartsTogether and start their writing journey with the community. The user will be able specify if they would like create a public account or remain anonymous. The user will be required to create a username and password. Any additional personal information is optional. The profile contains a responsive profile picture and personal details such as name, last name, years of service, and branch.

### Features Left to Implement

- The implementation of a forum where users can discuss together about a selected topic.
- The ability to add comments and likes to blog posts and stories.
- The ability for a user to change the visibility of a profile to anonymous or public after it has been created.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

-  Anonymous functionality proved problematic.
- Getting the stories to display as we wished was difficult and could be improved.
- User profiles were difficult to put together and is an area for future development.

## Deployment

We deployed the app using render.com.  This took a while as initially we tried to deploy with heroku unsuccessfully.  We also tried railway and then render which took some time to build but which was successful after some time.

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

All images were from [unsplash](https://unsplash.com/) and [pexels](https://www.pexels.com/) websites and were provided free.

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

### Content

-   All content was written by the developer team.

### Media

-   The hero image on the homepage is from https://unsplash.com/

### Acknowledgements

-   Tutor support at Code Institute for their support.
