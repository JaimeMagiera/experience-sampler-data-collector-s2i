# Experience Sampler Data Collector s2i

This repository contains the files necessary to build a container for the data collector component of the [Experience Sampler](http://www.experiencesampler.com) system using Red Hat's [Source-to-Image](https://github.com/openshift/source-to-image) tool. The image can built and hosted on Red Hat OpenShift or the upstream OKD. 

## Project Details ##
The Experience Sampler Data collector parses submissions, in the form of HTTP GET requests, from the Experience Sampler applications (iOS, Android), and writes the resulting data to disk. The Data Collector itself is a perl cgi script. It resides in the [/prod/prod-app/cgi-bin/](https://github.com/JaimeMagiera/experience-sampler-data-collector-s2i/tree/main/prod/prod-app/cgi-bin) folder of this respository. The script utilizes an Apache environmnent variable, which is initially defined as a container environment variable, to construct a path for the data files to reside. The files can be saved to external storage by attaching a storage mount to the container, and setting the appropriate path via the DATA_DIR environment variable.   


## Building the Container ##
There are two ways to build the container in OKD/Openshift:

* **Web Console:** Create a new project in the web console. Under the **Workloads** tab of the project, create a new item of type **Git Repository**  

* **Command Line:** Using the oc command, you can create a new project, then create a new application from the respository.
> oc new-project `<projectname>`

> oc new-app https://github.com/JaimeMagiera/experience-sampler-data-collector-s2i.git
 
For more information on bulding and running applications in OKD/OpenShift, see the [OKD documentation](https://docs.okd.io/latest/applications/application_life_cycle_management/creating-applications-using-cli.html)

## Utilities ##
This repository also contains several utilities that you can use to test your data collector.  

**test-data-collector.sh**[test-data-collector.html] This shell script simulates a survey submission to your data collector. Use the **-s** flag to provide the URL.

**test-data-collector.html** is  webpage with embedded javascript that simulates a survey submission. Enter the data collector URL in the form.

