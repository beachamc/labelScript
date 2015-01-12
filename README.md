# labelScript
A short script to generate labels in html

I created this script to be used to easily create labels for iPhones/iPads/Computers at the Apple Store.

## Dependencies
This project makes use of a package.json file that will install some of the dependencies. To use this you need to have [Node.js](http://nodejs.org/download/) installed. Then, simply type ```npm install``` from within the project's root directory.

This will install the following dependencies:
* [Grunt ~0.4.5](http://gruntjs.com/)
  * [Grunt Watch ~0.6.1](https://www.npmjs.com/package/grunt-contrib-watch)
  * [Grunt Compass ~0.9.1](https://www.npmjs.com/package/grunt-contrib-compass)
  * [Grunt Uglify ~0.5.1](https://www.npmjs.com/package/grunt-contrib-uglify)
* [MatchDep ~0.1.2](https://www.npmjs.com/package/matchdep)

Next, you will need [Ruby](https://www.ruby-lang.org/en/documentation/installation/) so that you can install [SASS](http://sass-lang.com/) by using the command ```sudo gem install sass```

Finally, this project uses [Python 2.7.X](https://www.python.org/downloads/) for the actual script itself. 

## Using the script
Once you have everything set up, navigate to the scripts root directory in terminal/command prompt and run the create_labels.py script using ```python create_labels.py```

This will open up the Python GUI and the .csv file. Make the appropriate edits to the .csv file, save, and hit Generate. Your labels should now open up in your default browser.

## Syntax for the .csv file
The Products.csv file contains columns for SKU, DEVICE TYPE, COLOR, CARRIER, SIZE, SPECS, NAME, and # OF LABELS. If any of the columns do not apply to the device you are inputting (ie Carrier for a Computer) simply put *n/a*

For Device Type, there are three options:

1.  IPHONE
2.  IPAD
3.  CPU

These will determine the size of the label and the formatting of the text.

For Color, there are the following options:

1. SPACEGRAY
2. SILVER
3. GOLD
4. WHITE
5. YELLOW
6. BLUE
7. GREEN
8. PINK

It is worth noting that the Computers have a default of White background so this field can be left as *n/a*

For Carrier, iPads will have:

1. WIFI
2. CELLULAR

And iPhones will have:

1. UNLOCKED
2. AT&T
3. VERIZON
4. SPRINT
5. T-MOBILE

The Specs column is only applicable for CPU Device Type and is of the format:

``` Processor | Screen Size | Ram | HD Size ```

Name is mostly important for the computers, however, it is also important in determining the label size difference between the iPhone 5c, 5s, and 6/6+

Finally, the # of Labels column specifies how many of each label to generate. This can be used if there needs to be labels on multiple sides of a shelf.
