# Automated App Engine Deployment

# Creating a New Project

We will start by creating a new project on Google Cloud.

1. To begin, navigate to the **Google Cloud Console** dashboard (**[https://console.cloud.google.com/](https://console.cloud.google.com/)**) and create a new project.
2. Once the project has been created, enable the **Cloud Source Repositories API** by searching for it in the search bar.

![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled.png)

Cloud Source Repositories are private Git repositories hosted on Google Cloud.

## Creating a Repository

The standard way to complete this task, is to use the **Google Cloud CLI** and have **Git** installed on your local system. However, to avoid any potential installation issues, we will utilize the **Google Cloud Shell**, which comes equipped with **gcloud** and Git.

1. To open the Google Cloud Shell, click the "**Activate Cloud Shell**" button located on the top right of the navigation bar.
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%201.png)
    
2. To ensure that our **Cloud Platform project** is set to the correct project, verify that the yellow text matches the **Project ID** for the newly created project. If a different project is set, enter the following command into the terminal to change to the correct project:
    
    ```
    gcloud config set project [PROJECT_ID]
    ```
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%202.png)
    
3. Create a ************************************************Google Cloud Repository************************************************ by entering the following command into the terminal and authorise the cloud shell if prompted:
    
    ```
    gcloud source repos create hello-world
    ```
    
4. Then, clone the repository by entering the following command into the terminal:
    
    ```
    gcloud source repos clone hello-world
    ```
    
    If the process is successful, you will receive the following message from the terminal: 
    
    ```
    Project [PROJECT_ID] repository [hello-world] was cloned to 
    [/home/USERNAME/hello-world]).
    ```
    

## Creating a Basic Flask App

1. To change to the “hello-world” directory, enter the following command into the terminal:
    
    ```
    cd hello-world
    ```
    
2. We need to create a **Python** file within our directory. To do this, enter the following command into the terminal:
    
    ```
    touch main.py
    ```
    
3. To build our Python file, we will use the command line text editor **Vim**. To do so, enter the following command into the terminal:
    
    ```
    vim main.py
    ```
    
4. To insert code using Vim, we must enter insert mode by typing "i" and then enter our Python code (See below). Once finished, press the "Esc" key to exit insert mode and type ":wq" to write and exit the Python file.
    
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8080, debug=True)
    ```
    

## Creating a Requirements File

1. To keep track of the libraries used in our Python project, we will create a requirements file. 
    
    ```
    touch requirements.txt
    ```
    
2. Similar to the previous step, to edit this file, we will again use Vim.
    
    ```
    vim requirements.txt
    ```
    
3. Add the following code to our requirements file:
    
    ```
    Flask==2.1.0; python_version > '3.6'
    Flask==2.0.3; python_version < '3.7'
    gunicorn==20.1.0
    ```
    

## Creating a YAML File

For this project we will use a .**yaml** file. A .yaml file in a project is used to configure the deployment settings for the app, such as the **runtime environment** and **entry point**. 

1. Enter the following code to create our .yaml file:
    
    ```
    touch app.yaml
    ```
    
2. We will also use Vim to edit our YAML file.
    
    ```
    vim app.yaml
    ```
    
3. Enter the following code to our YAML file:
    
    ```yaml
    runtime: python
    env: flex
    entrypoint: gunicorn -b :$PORT main:app
    
    runtime_config:
      python_version: 3
    
    manual_scaling:
      instances: 1
    resources:
      cpu: 1
      memory_gb: 0.5
      disk_size_gb: 10
    ```
    

## Pushing to Cloud Source Repository

1. To prepare the changes made to our local repository for committing to the remote repository, we will use the `git add` command to add changes to the **staging area**.
    
    ```
    git add .
    ```
    
2. Use the following code to commit our changes to the local repository and attach a message:
    
    ```
    git commit -m "Add Flask app to Cloud Source Repositories"
    ```
    
    You may be prompted to identify yourself before the commit can complete, in which case you should enter the commands below and commit again.
    
    ```
    git config --global user.name "NAME"
    git config --global user.email "EMAIL"
    ```
    
3. Finally, to push our committed changes to the remote Cloud Source Repository, use the `git push` command and accept any prompts to authenticate.
    
    ```
    git push origin master
    ```
    
4. If the process is successful, you should receive output similar to this:
    
    ```
    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 679 bytes | 679.00 KiB/s, done.
    Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
    To URL_TO_CLOUD_SOURCE_REPOSITORY
     * [new branch]      master -> master
    ```
    
    At the bottom of the output, there should be a URL for the repository. Click on that link or navigate to **[https://source.cloud.google.com/repos](https://source.cloud.google.com/repos)** to view your repository. Inside the repository, you should see the three files we created.
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%203.png)
    

## Deploying our App

Now that we have created a repository in Cloud Source Repositories with a small Python app, we will now deploy our app from Cloud Source Repositories to App Engine. After deploying the initial app, we will update the app's code and the associated repository, and redeploy the updated code.

Enable the **App Engine Admin API** by searching for it in the search bar.

1. To deploy our app, enter the command below into the terminal. Authorize any necessary prompts and select a region to deploy the application. The closest region is europe-west2, which is located in London (Be aware, the deployment process may take a few minutes to complete).
    
    ```
    gcloud app deploy app.yaml
    ```
    
2. Once the deployment is finished, enter the following command into the terminal to obtain a URL for our deployed app:
    
    ```
    gcloud app browse
    ```
    
3. Navigating to the URL should lead you to a blank web page with the text "Hello, World!" displayed.
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%204.png)
    

## Updating our App

1. To update our app, we will use Vim to modify the return message.
    
    ```
    vim main.py
    ```
    
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'Goodbye, World!'
    
    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8080, debug=True)
    ```
    
2. Add the modified Python file to the staging area.
    
    ```
    git add main.py
    ```
    
3. Commit our modified Python file with an appropriate message. 
    
    ```
    git commit -m "Update message in hello function in main.py"
    ```
    
4. Then, push the changes to our remote Cloud Source Repository.
    
    ```
    git push origin master
    ```
    

## Redeploying our App

1. To redeploy the app, enter the command for deploying the app in the terminal once more:
    
    ```
    gcloud app deploy app.yaml
    ```
    
2. After the deployment is complete, open the redeployed app by using the following command and clicking on the returned URL:
    
    ```
    gcloud app browse
    ```
    

## Automating Deployment

We have now manually redeployed our app after updating our app stored in the Cloud Source Repository. We will now setup automatic deployment for our app using **********************Cloud Build Triggers**********************.

We now need to enable the **Cloud Build API** by searching for it in the search bar.

## Enabling Identity and Access Management (IAM) Roles

1. Open the **Cloud Build Settings** page by searching for it in the search bar.
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%205.png)
    
2. Upon navigating to the **Service account permissions** page, set the status of the **App Engine Admin** role to "Enabled".
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%206.png)
    

## Creating a YAML File

We have already created an app.yaml file, which we used to configure the settings for an app we deployed using App Engine. We now need to create a cloudbuild.yaml file, which we will use to configure the steps for a Cloud Build pipeline.

A cloudbuild.yaml file typically includes information such as the build triggers, the actions to be taken during the build process, and the environment variables that should be set during the build.

We shall repeat the steps we took when we created our app.yaml file:

1. Create a file named "cloudbuild.yaml”.
    
    ```
    touch cloudbuild.yaml
    ```
    
2. Use Vim to insert the configuration information below:
    
    ```
    vim cloudbuild.yaml
    ```
    
    ```yaml
    steps:
    - name: "gcr.io/cloud-builders/gcloud"
      args: ["app", "deploy"]
    timeout: "1600s"
    ```
    

## Pushing to Cloud Source Repository

1. Add our new “cloudbuild.yaml” file to the staging area.
    
    ```
    git add cloudbuild.yaml
    ```
    
2. Commit it with an appropriate message. 
    
    ```
    git commit -m "Add cloudbuild.yaml file"
    ```
    
3. Finish off by using the git push command to push the updated contents of the local Git repository to Cloud Source Repositories.
    
    ```
    git push origin master
    ```
    

## Creating a Build Trigger

1. Open the **Cloud Build Triggers** page by searching for it in the search bar.
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%207.png)
    
2. Click Create Trigger (Make sure you are in the correct project), and fill out the following options:
    - In the Name field, enter a suitable name for your trigger and select “europe-west1” for the Region dropdown.
    - In the Event section, check “Push to a branch”.
    - In the Source section, for the Repository dropdown, select our “hello-world” Cloud Source Repository and select `^master$` for the Branch field.
    - In the Configuration section, check “Cloud Build configuration file (YAML or JSON) for Type and check “Repository” for location. In the Cloud Build configuration file location field, enter `/cloudbuild.yaml`
3. Click the Create button to complete the process for building our trigger.

## Modifying and Pushing our App

1. We need to update our app again, we will use Vim to modify the return message.
    
    ```
    vim main.py
    ```
    
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return "Hello, World! I'm back and deploying automatically after every push."
    
    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8080, debug=True)
    ```
    
2. Add the modified Python file to the staging area.
    
    ```
    git add main.py
    ```
    
3. Commit our modified Python file with an appropriate message. 
    
    ```
    git commit -m "Update message in hello function in main.py"
    ```
    
4. Then, push the changes to our remote Cloud Source Repository.
    
    ```
    git push origin master
    ```
    

## Confirming Successful Deployment

1. Reopen the **Cloud Build Triggers** page by searching for it in the search bar.
2. On the left side,click the “History” tab (make sure the correct project is selected and the Region “europe-west1” is selected (if you chose that region in the previous step)).
3. There should be a new entry at the top of the list of builds (You can either wait for the build to complete or you can click on the “Build ID” to see the build in real time.
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%208.png)
    
4. If a green checkmark appears, then our build is successful. After which we can use the `gcloud app browse` command in the terminal to get the URL for our deployed app and see the updated app deployed.

    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%209.png)
    
    ```
    gcloud app browse
    ```
    
    ![Untitled](Automated%20App%20Engine%20Deployment%20faf490d1e50a4fe5ba4c127722377e0a/Untitled%2010.png)
