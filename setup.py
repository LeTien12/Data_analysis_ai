from setuptools import find_packages , setup

setup(
    name = "Data Analysis",
    version =  '0.0.1',
    author= 'TienLe',
    author_email='tle38413@gmail.com',
    install_requires = ['pandas' , 'streamlit' , 'matplotlib' , 'python-dotenv' , 'seaborn', 'langchain-google-genai' , 'langchain-experimental' , 'pygwalker' , 'tabulate'],
    packages=find_packages()
)