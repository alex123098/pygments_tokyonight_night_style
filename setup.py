from setuptools import setup, find_packages

setup(name="tokyonight-night-pygments",
      description="Pygments style based on the Tokyonight color scheme.",
      packages=find_packages(),
      entry_points="""
                   [pygments.styles]
                   tokyonight = tokyonight.style:TokyonightNightStyle
                   """
      )
