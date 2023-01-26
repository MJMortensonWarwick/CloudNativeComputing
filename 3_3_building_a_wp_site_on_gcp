# Deploying a WordPress Website on GCP

# Introduction

Hello all, and welcome to this tutorial on deploying a WordPress website using Google Cloud Platform. In this tutorial, we will use the powerful tools and resources provided by Google Cloud to set up and launch our own WordPress website.

Recently, I have been studying and working to acquire new skills. The idea of starting a personal blog to document my progress and learning crossed my mind. This tutorial will guide you through the process of setting up your own WordPress website, which you can use as a personal blog or a professional portfolio to showcase what you have learned during your master's course.

# Create Project & Enable API’s

The first step in deploying a WordPress website using Google Cloud Platform is to create a new project and enable the necessary API's. Specifically, we will be enabling the Compute Engine API,  Cloud DNS API, Cloud Deployment Manager V2 API, and Cloud Runtime Configuration API. 

1. Go to the Google Cloud Console ([https://console.cloud.google.com/](https://console.cloud.google.com/)).
2. Create a new project by clicking on your current project in the top left corner of the navigation menu and selecting ‘NEW PROJECT’ in the top right corner of the box that appears.
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled.png)
    
3. Search the following API’s in the console search bar and select and enable them:
    - `Compute Engine API`
    - `Cloud DNS API`
    - `Cloud Deployment Manager V2 API`
    - `Cloud Runtime Configuration API`

We now have a new project with the necessary API's enabled, ready for the next steps in the tutorial.

# Launching WordPress

The next step is to launch WordPress from the marketplace. The Google Cloud Marketplace offers a variety of pre-configured software solutions that can be easily deployed to a Google Cloud project. The benefit of launching WordPress from the marketplace, is that we can save time and effort on the setup and configuration of the software, as it has already been done for us.

1. Search `Marketplace` in the console search bar, and select the one with the shopping cart icon (There are multiple Marketplace pages).
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%201.png)
    
2. In the Marketplace search field search for `WordPress`.
3. There will be numerous WordPress options for you to choose from, select the option that has ‘Google Click to Deploy - Virtual machines’ in the subtitle.
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%202.png)
    
4. On the WordPress page select ‘Launch’ and it should check our API’s and take us to the deployment settings.

We have now launched WordPress from the marketplace, in the next step we will deploy the instance.

# Deploying WordPress Instance

In this step, we will configure the settings for the instance, including the machine type, disk size, and network settings. However, for simplicity's sake, we will retain the default settings recommended by Google and only fill in some missing details.

1. In the ‘Deployment name’ field, we need to enter a name for our instance and underneath we should ensure the zone is set to a zone in europe-west (In reality, you may choose a different zone if you expect your main traffic to come from a different region).
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%203.png)
    
2. For the ‘Administrator e-mail address’ field, you will need to enter your email address.
3. Finally scroll down to the bottom of the page and ensure ‘I accept the GCP Marketplace Terms of Service’ is checked before selecting ‘DEPLOY’.
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%204.png)
    

# Accessing our WordPress Website

Now that we have successfully deployed our WordPress website, the next step is to access it. WordPress should have provided us with our site's address, admin login URL, and all the necessary usernames and passwords. To confirm that our site has been deployed, we can click on the provided links. If your browser gives a warning about a non-private connection, you can change "https" to "http" in the search bar.

![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%205.png)

![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%206.png)

# Assigning a Static IP Address

Currently, the website's URL is an IP address. However, this IP address is ephemeral, meaning it is temporary and can change. This is not ideal if we want to access the site without having to look up the current IP address on the Google Cloud Platform. To resolve this, we can reserve a static IP address.

1. 1. Search for and select `IP addresses` in the console search bar.
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%207.png)
    
2. Select the ‘External IP Addresses’ tab in the menu bar.
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%208.png)
    
3. You should see our VM instance in the "In use by" column (it will have the deployment name you entered previously).
4. Make a note of the IP address (it's in the "IP address" column on the left side).
5. On the right side, you will see the option to "Reserve." Select the reserve button.
6. A box will appear. Enter a name for your IP address and select the reserve button to reserve our static IP address.
    
    ![Untitled](Deploying%20a%20WordPress%20Website%20on%20GCP%20ee8287d0f96b49e2bbfb1dbf9985d882/Untitled%209.png)
    

We now have a permanent IP address to access our WordPress site, and that concludes the tutorial. As a reference for the future, if you are interested in connecting your hosted WordPress site to a domain name you have purchased, you can refer to the videos in the Extra Resources section. The latter video provides more detailed information.

# Deleting Our Instance

To prevent you using up all of your credits, you can delete the WordPress deployment by following these steps:

1. Search and select `Deployment Manager` in the search bar.
2. Check the checkbox for the deployment and select the delete button in the menu bar, and delete all of the resources associated with this deployment.

If you want to create a WordPress website using Google Cloud Platform for your personal blog/portfolio, I recommend redeploying the WordPress site, but using an ec-2 micro instance and experimenting with some of the lower-cost zones. This should allow you to host your website for free or at very least at very low costs.

# Extra Resources

## Videos

[https://youtu.be/mcwYGpdKDEg](https://youtu.be/mcwYGpdKDEg)

[https://youtu.be/_g0yxRdMpTk](https://youtu.be/_g0yxRdMpTk)
