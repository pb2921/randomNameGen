import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='randomNameGenerator',  
     version='0.1',
     scripts=['randomName.py'] ,
     author="Priyanshu Bhatt",
     author_email="priyanshu2921@gmail.com",
     description="A random number generator package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/pb2921/randomNameGen",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
