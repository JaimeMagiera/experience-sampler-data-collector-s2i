# Experience Sampler Data Collector s2i

This repository contains the files necessary to build a container for the data collector component of the [Experience Sampler](http://www.experiencesampler.com) system using Red Hat's [Source-to-Image](https://github.com/openshift/source-to-image) tool. The image can built and hosted on Red Hat OpenShift or the upstream OKD. 

## Building the Container ##
There are two ways to build the container in Openshift:

* Web Console: Create a new project in the web console. Under the **Workloads** tab of the project, create a new item of type **Git Repository**For more information, see the [OKD documentation](https://docs.okd.io/latest/applications/application_life_cycle_management/odc-creating-applications-using-developer-perspective.html) 

* Command Line: Using the oc command, you can create a new project from the respository.
> oc new-app https://github.com/JaimeMagiera/experience-sampler-data-collector-s2i.git
 
 For more information, see the [OKD documentation](https://docs.okd.io/latest/applications/application_life_cycle_management/creating-applications-using-cli.html)
