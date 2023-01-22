# Cloud Native Labs: Google Cloud Platform Demo

### Introduction

This book provides an introduction to the Google Cloud Platform (GCP). We will create a Linux Virtual Machine set to our chosen configuration and install and run various software on that machine.

### Docker

Using Docker is a necessary component of completing this tutorial. The most user friendly way to achieve this is by using the Docker Desktop application. Unfortunately due to Docker Desktop requiring certain versions of Windows operating systems, using Docker Desktop may not be feasible for everybody. A way to circumvent this issue is by running Docker via a virtual machine and installing a Linux operating system. This method can be quite intensive on a machines resources, having to essentially store and run two operating systems at the same time, as well as require the installation of additional software. 

This provides us with a wonderful opportunity to utilise a virtual machine instance on the cloud, which we will do using GCP Compute Engine to launch a Linux virtual machine instance hosted on a Google server.

#### Creating a VM Instance on GCP

Our first step is to log into Google Cloud and go to the GCP Console.

![GCP Dashboard](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/a2e787456015c8f2ac9e7d35b7f652f3ac45bf43/images/gcp-dashboard.PNG)

We will start by creating a project for our walkthrough. To create a new project you click your current project that is located on the left side of the top navigation bar and click the **new project** button .

![Create New Project](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/gcp-new-project.png)

We can give our project an appropriate name and then click the **create** button.

![Create New Project](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/gcp-create-project.png)

From here we can either click the side menu and hover over **Compute Engine** and click **VM instances** or search for **VM instances** in the search bar.

![GCP Menu - VM instances](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/vm-instances-menu.png)

![GCP Search - VM instances](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/vm-instances-search.PNG)

If this is the first time accessing Compute Engine for your project you may need to approve it, after you should see the VM instances for your project, as this is our first instance it should be empty, so we will need to create an instance, which we can do by clicking the  **Create Instance** button.

![Create Instance Button](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/create-instance.PNG)

On the create an instance page we have numerous options to choose from, feel free to rename your instance to something more appropriate. One of the first things we should notice is the region option, the region we choose is where our resources will be hosted and this choice is important for multiple reasons. To save costs we will be hosting our resources on a single region and zone, and to decrease network latency we will choose a region close to us, such as one of the **Europe West** regions. We will select ***europe-west1 (Belgium)***, although the ***europe-west2 (London)*** is closer to us, another one of our considerations is cost and the London server has a higher hourly cost than the one in Belgium. You can choose any of the zones, it is of little consequence for our scenario.

The next thing we need to change is our **Machine Configuration**, we are currently using an E2 machine in the  **General-Purpose** machine category. There are different hardware options available depending on your needs and requirements, the basic E2 machine is fine for us but we will change the **Machine type** from ***e2-medium(2 vCPU, 4GB memory)*** to ***e2-micro(2 vCPU, 1GB memory).***  The ***e2-micro*** machine has only a quarter of the memory as the ***e2-medium*** machine and the cost reflects this by being quartered also. 

![Machine Configuration](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/vm-instance-machine-configuration.PNG)

Scroll down further and we will reach the **Boot disk** section and click the **Change** button. Here is where we can choose what operating system we want to load onto our instance, and how much storage we wish to dedicate to our VM.  There are many advanced configurations which we do not need to concern ourselves with, it is worth knowing that their are multiple boot disk types available to us, whether you want a standard hard disk drive (HDD) or a choice of multiple solid-state drive (SSD) options. The choice of disk type will often come down to what actions you wish to perform on your machine, we will just go with one of the affordable options and keep **Balanced persistent disk**. We will change our operating system from **Debian** to **CentOS** version **7** and we will increase our **disk size** from **10GB** to **25GB** to allow for the installation of CentOS which requires more hard disk space compared to some of the lighter Linux OS alternatives.

![Boot Disk](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/vm-instance-boot-disk.PNG)

We can then scroll down to the bottom of the page, ignoring the other configuration options as they are not relevant to us for this task and click the **create** button.

![Creating VM Instance](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/gcp-final-create-instance.png)

After a short while, our VM instance should be created and initialised and ready for us to access. It is super simple to connect to our Linux VM using the Google Cloud Console by clicking on the SSH button on our instance. 

![Initialised VM](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/gcp-ssh-instance.png)

![Connecting to VM](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/connecting-to-instance.png)

![Connected to VM](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/connected-to-instance.png)

After successfully connecting to our Linux VM we can see the terminal. (If you want to increase the font size you can do so by clicking on the cog and changing the font size setting).

We will now install some of the necessary libraries and software for this module. We’ll begin by updating the core Linux packages:

```sudo yum update```

“sudo” (which stands for super-user do) means that we will use admin privileges to do the updates. “yum” (Yellowdog Updater, Modified) is a package manager for many flavours of Linux (In our case CentOS). You may need to use a different package manager for other operating systems and the commands will be different.

You will be prompted to confirm you want to do these installations which you can do by typing “y” into the console. If its successful it should tell you so:

![Updating Core Linux Packages](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/sudo-yum-update.png)

Next we will install Docker, again using yum (and again you need to type “y” to confirm):

```sudo yum install docker```

Once installed we will start Docker and “enable” it. This latter command means that, using Linux’s system service manager, Docker will be setup to start automatically if our instance were to reboot:

```
sudo systemctl start docker
sudo systemctl enable docker
```

Finally we will install Python 3 on to the machine (again, type “y” when prompted):

```sudo yum install python3```

To verify that Docker is working properly, we can run the standard “Hello World” test:

``` sudo docker run hello-world```

which should produce the following output:

![Docker Hello World](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/docker-hello-world.png)

We can do the same for Python3 and verify that our installation was successful, writing everyone's favourite "Hello World! program:

```python```

```print("Hello World!")```

![Python Hello World](https://raw.githubusercontent.com/Jordan-Bruno/cnc-workbook/main/images/python-hello-world.png)
