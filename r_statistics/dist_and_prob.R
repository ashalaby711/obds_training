###Query distributions and probablities###
#Plot the cumulative distribution function in the range [-5,5]
q <- seq(-5,5, by=0.1)
vector_probabilities <- pnorm(q, mean=0, sd=1)
plot(x=q, y=vector_probabilities)
q
vector_probabilities

#Plot the inverse cumulative distribution function for quantiles in 0.01 increment
p <- seq(0,1, by=0.01)
p
vector_values <- qnorm(p, mean = 0, sd=1)
vector_values
plot(x=p, y=vector_values)

#Plot the density function in the range [-5,5]
vector_density <- dnorm(q, mean=0, sd=1)
vector_density
plot(x=q, y=vector_density)
#What is the probability of observing a value greater than 2?
greater_than_2 <- 1-pnorm(2)
greater_than_2
#2.28
#What is the probability of observing a value between -2 and 2?
between_2 = pnorm(2) - pnorm(-2)
between_2
#What is the probability of observing a value more extreme than -2 or 2?
extreme <- pnorm(-2) + (1-pnorm(2))
extreme

#Use the ecdf() function to compute the empirical cumulative distribution function for the variable
#Sepal.Length in the iris data set
iris

iris_ecdf <- ecdf(iris$Sepal.Length)
str(iris_ecdf)

#Use the plot() function to visualise the empirical cumulative distribution function.
plot(iris_ecdf)

#Use the knots() function on the ecdf output and compare this with the list of unique values for the
#variable Sepal.Length
unique(iris$Sepal.Length) #getting the unique values -unsorted-
knots(iris_ecdf) #getting the unique values sorted
sort(unique(iris$Sepal.Length)) #same as knots function
iris_ecddf(6) #probability of value less than 6

#Use the summary() function to view some information about each column
summary(iris)
summary(iris$Sepal.Length)
summary(iris$Sepal.Width)
summary(iris$Petal.Length)
summary(iris$Petal.Width)
summary(iris$Species)

#Visualise the distribution of Sepal.Length , stratified by species
par(mfrow=c(2,2))
hist(iris[iris$Species =="setosa",]$Sepal.Length, breaks=10, labels= FALSE, main=NULL, col= "red")
hist(iris[iris$Species =="versicolor",]$Sepal.Length, breaks=10, labels= FALSE, main=NULL, col= "green")
hist(iris[iris$Species =="virginica",]$Sepal.Length, breaks=10, labels= FALSE, main=NULL, col= "blue")

#Trials:
#plot(x=iris$Species, y=iris$Sepal.Length)
#plot(iris$Sepal.Length)
#shapiro.test(iris$Sepal.Length)
#sepal_length_setosa <- c(iris$Sepal.Length & iris$Species == "setosa")
#sepal_length_setosa

par(mfrow=c(1,1))
plot.new()
plot.window(xlim= c(4.3, 7.9), ylim= c(0,2))
lines(density(iris[iris$Species == "setosa",]$Sepal.Length), col= "red")
lines(density(iris[iris$Species == "versicolor",]$Sepal.Length), col= "green")
lines(density(iris[iris$Species == "virginica",]$Sepal.Length), col= "blue")
range(iris$Sepal.Length)
axis(side=1, at=seq(4,8))
axis(side=2, at=seq(0,2,0.2))


shapiro.test(iris$Sepal.Length)
shapiro.test(iris[iris$Species == "setosa",]$Sepal.Length)
shapiro.test(iris[iris$Species == "versicolor",]$Sepal.Length)
shapiro.test(iris[iris$Species == "virginica",]$Sepal.Length)

#is there a significant variant between species in sepal length
anova_iris <- aov(Sepal.Length ~ Species, data=iris)
summary(anova_iris)
kruskal_iris <- kruskal.test(Sepal.Length ~ Species, data=iris)
kruskal_iris

#running tukeys test for multiple comparison
tukey_test <- TukeyHSD((anova_iris))
str(tukey_test)
View(tukey_test$Species)
