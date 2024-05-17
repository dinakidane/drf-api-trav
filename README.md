<h1  align="center">A Global Affair</h1>

**A Global Affair** is a captivating travel blog dedicated to sharing the wonders and adventures of exploring the world. It chronicles the journeys of a passionate traveler who seeks to uncover the beauty, culture, and unique experiences that each destination has to offer. From bustling cityscapes to serene natural landscapes, "A Global Affair" offers insightful travel tips, inspiring stories, and practical advice to fellow wanderers. The blog emphasizes the importance of cultural immersion, sustainable travel, and personal growth through exploration. Whether you're a seasoned globetrotter or an aspiring adventurer, **A Global Affair** aims to inspire and guide you on your own travel endeavors, making every trip a memorable and enriching experience.

## Agile Methodology

- Agile methodology is an approach to project management and software development that emphasizes flexibility, collaboration, and customer satisfaction. It involves breaking down projects into smaller, manageable tasks, which are then completed in short iterations or sprints. This method allows for continuous improvement and adaptability to changing requirements.

- In this project, Agile methodology was used to create and manage project boards on GitHub. The tasks were organised into three columns: 'To Do', 'In Progress', and 'Done'. This setup helped clear up the status of each task and prioritize the work efficiently. By regularly updating the board, it was ensured that all tasks were tracked and completed systematically. Over time, this approach kept everything organized and provided a clear overview of what needed to be done, what was in progress, and what was already completed. This continuous tracking and updating process allowed the project to work smoothly and ensured that nothing was overlooked.

![Project Board](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715925622/Screenshot_2024-05-17_at_06.38.36_rvagje.png)

## User stories

### Navigation & Authentication

1. Navigation (Navbar):
    - As a user, I want a navigation bar accessible on all pages so that I can switch between pages easily.

2. Routing:
    - As a user, I want to navigate between pages quickly to browse content smoothly without reloading.

3. Authentication (Sign up):
    - As a user, I want to register for a new account so that I can access all the features available to registered users.

4. Authentication (Sign in):
    - As a user, I want to log in to the app so that I can utilize the features available to logged-in users.

5. **Authentication (Logged-in Status):**
    - As a user, I want to know if I'm logged in or not so that I can log in if necessary.

6. **Authentication (Refreshing Access Tokens):**
    - As a user, I want to stay logged in until I choose to log out, ensuring an uninterrupted user experience.

7. **Navigation (Conditional Rendering):**
    - As a user who's logged out, I want to see options to sign in or sign up so that I can access the app's features.

8. **Avatar:**
    - As a user, I want to see avatars of other users so that I can identify them easily within the application.

### Posts

9. **View Post Page:**
    - As a user, I want to access the post page so that I can read comments about a particular post.

10. **Edit Post:**
    - As the creator of a post, I want to edit the title and description so that I can make corrections or updates to it after publishing.

11. **Add Comment:**
    - As a logged-in user, I want to add comments to a post so that I can share my opinions on it.

12. **Comment Timestamp:**
    - As a user, I want to see how long ago a comment was made so that I can gauge its relevance.

13. **Read Comments:**
    - As a user, I want to read comments on posts so that I can see what others think about them.

14. **Delete Comment:**
    - As the author of a comment, I want to delete it so that I can remove it from the platform.

15. **Edit Comment:**
    - As the author of a comment, I want to edit it so that I can update or correct it.

### Profiles

16. **View Other Users' Profiles:**
    - As a user, I want to view other users' profiles so that I can see their posts and learn more about them.

17. **Popular Profiles:**
    - As a user, I want to see a list of the most followed profiles so that I can discover popular content creators.

18. **User Profile Stats:**
    - As a user, I want to see details about a specific user like their bio, number of posts, followers, and accounts they follow so that I can understand more about them.

19. **Follow/Unfollow User:**
    - As a logged-in user, I want to follow or unfollow other users so that I can customize my feed based on whose posts I want to see.

20. **View All Posts by User:**
    - As a user, I want to view all posts made by a particular person so that I can catch up on their latest content or decide whether to follow them.

21. **Edit Profile:**
    - As a logged-in user, I want to update my profile so that I can change my picture and bio.

22. **Update Username and Password:**
    - As a logged-in user, I want to change my username and password so that I can modify my display name and keep my profile secure.


### Adding and favouriting a post

23. **Create Posts:**
    - As a logged-in user, I want to create posts so that I can share my images with the community.

24. **View Single Post:**
    - As a user, I want to view the details of a specific post so that I can understand it better.

25. **Like Post:**
    - As a logged-in user, I want to like posts so that I can express support for the content I find interesting.

### Posts

24. **View Recent Posts:**
    - As a user, I want to see the most recent posts ordered chronologically, so I can stay updated with the latest content.

25. **Search Posts:**
    - As a user, I want to search for posts using keywords so that I can find the content and profiles that interest me the most.

26. **View Liked Posts:**
    - As a logged-in user, I want to see the posts I liked so that I can revisit the content I enjoy.

27. **View Followed Users' Posts:**
    - As a logged-in user, I want to see posts from the users I follow so that I can stay informed about their latest updates.

28. **Infinite Scroll:**
    - As a user, I want to scroll through the site's images with automatic loading so that I can browse without needing to click "next page."

## Features

### Navigation

- The navigation bar features a sleek and minimalist design that enhances the user experience. It changes its appearance based on whether you are logged in or not. On tablets and mobile devices, it turns into an easy-to-use hamburger menu.

- ![Navbar](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715927747/Screenshot_2024-05-17_at_07.34.59_pwekri.png)

- When a user is logged out, the navigation bar includes the following items:
    - Logo: Always visible, this logo links back to the homepage.
    - 'A Global Affair': This menu item takes users to the "Home" section, showcasing a variety of posts.
    - Authentication: Prominently displayed "Sign In" and "Sign Up" icons provide quick access to the login and registration processes.

- ![Navbar](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715928055/Screenshot_2024-05-17_at_07.40.48_ryqgv4.png)

- When a user is logged in, more options become available:
    - 'Travel' Feed : Users can explore content from profiles they follow, favorite posts, reply to posts, and subscribe to content.
    - Authentication: The authentication icons change to show a link to the user's profile page and a "Sign Out" option for easy exit.
    - Favourites: This page displays all the posts the user has liked.

### Authentication

![Sign Up](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715928307/Screenshot_2024-05-17_at_07.44.59_z3uidu.png)

- Users who haven't created an account can click on the "Sign Up" link in the navigation bar to register. The registration process follows the standard dj-rest/auth/registration method.

![Sign In](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715928300/Screenshot_2024-05-17_at_07.44.40_gtwhen.png)

- If a user already has a Cool the Earth account, they can click on the "Sign In" option in the navigation bar to log in.

### Global Affair section / Homepage

#### Popular Profiles

- The Popular Profiles Component is a standout feature across the site. On larger screens, it is displayed on the right side of every page, while on smaller screens, it is located at the top. 
- This component ranks users based on their subscriber count, showing the top ten profiles on larger screens and the top four profiles on smaller screens.

- ![Logged out Popular profiles](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715929130/Screenshot_2024-05-17_at_07.56.57_gtqqv3.png)

- For users who aren't logged in, the component shows the profile avatar and username. 

![Logged in User Popular Profiles](https://res.cloudinary.com/dgq43ynzg/image/upload/v1715929127/Screenshot_2024-05-17_at_07.57.10_dmfxib.png)

- Logged-in users, however, can also see follow and unfollow options next to each profile. Clicking on any profile avatar takes the user to that individual's complete profile page.

#### Searchbar


#### Posts