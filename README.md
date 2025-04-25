![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Happy Green Space

Happy Green Space is a web-based platform that aims to bring the following functionalities together in one space:

- The ability for the users to register to the platform and login
- The ability for the users to enter and store particular information about their plot
- The ability for the users to search and obtain information about plants
- The ability for users to join a converstation through a platform forum
- Regular updates of a page which provides information about the specific tasks to undertake in each month of the year.

With all these functionalities, the platform target to function as a home page for allotment users.

## App's Location

- Happy Green Space Live Link: 
  - <https://happy-green-space-94f206e157cb.herokuapp.com>
  - <https://happy-green-space-94f206e157cb.herokuapp.com/gossip_corner/>

- happy-green-space GutHub Repository:
  - <https://github.com/hisarciklilar/happy-green-space>
  
## User Experience

Happy Green Space is a platform targeting allotment users, although people who do gardening may also use it.

## User Stories

_**Account creation**_:

As a **Site User** I can **create/register an account** so that **I can participate in the plot holders' forum and also have my own account space where I can save a list of my plants and a wish list**.

-   **AC1** Given an email a user can register an account.\
-   **AC2** Then the user can log in.\
-   **AC3** When the user is logged in they can read posts in the forum.\
-   **AC4** When the user is logged in they can effectively use their personal space to create, edit and delete plant entries.

_**Read a post**_:

As a **Site User**, I can **read posts on the plot holders' forum** so that **I can join the conversation**.

-   **AC1** When the user is logged in, they can see and read the posts in the forum

_**Create a post**_:

As a **Site User**, I can **create posts on the plot holders' forum** so that **I can join the conversation**.

-   **AC1** When the user is logged in, they can create posts in the forum

_**Edit or delete a post**_:

As a **Site User**, I can **edit / delete my own posts on the plot holders' forum** so that **I can join the conversation**.

-   **AC1** When the user is logged in, they can edit (modify) their own posts in the forum
-   **AC2** When the user is logged in, they can delete their own posts in the forum

_**Delete a post (admin)**_:

As a **Site Admin** I can **delete posts of platform users** so that **I can remove offensive content**.

-   **AC1** When the admin is logged in, they can view the posts in the forum.

-   **AC2** When the admin is logged in, they can delete or edit posts in the forum.

_**Update plant database**_:

As a **Site Admin** I can **update the platform's plant database by adding new entries, editing existing ones and deleting entries when necessary** so that **the Site Users have a satisfactory search experience**.

-   **AC1** When the admin is logged in, they can add items to the plant database

-   **AC2** When the admin is logged in, they can modify the entries in the plant database

-   **AC3** When the admin is logged in, they can remove entries from the plant database

_**Follow platform searches**_:

As a **Site Admin** I can **see which plants are searched for in the platform** so that **I can prioritize addition of most commonly searched plants into the platform's plant database**.

-   **AC1** When the admin is logged in, they can see a list of searched items
-   **AC2** When the admin is logged in, they can see the date that the search was conducted
-   **AC3** When the admin is logged in, they can see the location that the search was conducted

_**Maintain a wish list**_:

As a **Site User**, I can **maintain a wish list** so that **I can easily remember the name of plants I like and I can better plan what to grow in the future.**

-   **AC1** Given a logged user, they can create a wish list

-   **AC2** Given a logged user, they can add items to the wish list

-   **AC3** Given a logged user, they can delete items from the wish list

-   **AC4** Given a logged user, they can edit list of items in the wish list

_**Create a visual representation of user's plot**_:

As a **Site User** I can **enter and save approximate measurements of my allotment/garden plot** so that **I can mark on a visual representation of my plot the plants I planted**.

-   **AC1** Given a logged user, they can see a rough visual (rectangular) representation of their plot

-   **AC2** Then they can mark on the plot where they planted

-   **AC3** Then they can mark on the plot what they planted

_**Keep a record of plantations**_:

As a **Site User**, I can **keep a record of plants I planted and the dates I planted them** so that **I can remember what harvest to expect and better plan future actions.**

-   **AC1** Given a logged user, they can create a list of planted plants

-   **AC2** Given a logged user, they can add items to the wish list

-   **AC3** Given a logged user, they can delete items from the wish list

-   **AC4** Given a logged user, they can edit list of items in the wish list

_**Obtain information about plants**_:

As a **Site User** I can **get information about plants I search on the platform** so that **I can make informed decisions on what to plant and to which spot in my plot**

-   **AC1** User can easily locate the search button

-   **AC2** User can enter plant's name in the search field

-   **AC3** User can press the search button, which triggers a search in the database

-   **AC4** User can see search results on screen

