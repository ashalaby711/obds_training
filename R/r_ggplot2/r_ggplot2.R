#initialise a new project environment
renv::init()

#install packages in the project environment
renv::install('ggplot2')

#save the current status of the project to the lock file
renv::snapshot()
#the message says that nothign to save
#doing something to snapshit it!
library(ggplot2)

renv::snapshot()

ggplot(diamonds)
ggplot(diamonds, aes(x = carat, y = price))
