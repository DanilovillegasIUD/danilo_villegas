

from setuptools import setup, find_packages

setup(
    name="Actividad_3",
    version="0.0.2",
    author="Danilo Villegas Restrepo",
    author_email="danilo.villegas@est.iudigital.edu.co",
    description="Evidencia de aprendizaje Numero 3",
    py_modules=["Actividad_3"],
    install_requires=[
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "requests"
    ]
    
    
)

