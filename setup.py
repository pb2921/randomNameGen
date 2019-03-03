import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='randomNameGen',  
     version='0.3',
     scripts=['randomName.py'] ,
     author="Priyanshu Bhatt",
     author_email="priyanshu2921@gmail.com",
     description="A random number generator package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/pb2921/randomNameGen",
     packages=setuptools.find_packages(),
	include_package_data=True,
	package_dir={'randomNameGen':'randomNameGen'}, # the one line where all the magic happens
     package_data={
      'randomNameGen': ['1000Names.txt','100lastNames.txt'],
     },
	classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
