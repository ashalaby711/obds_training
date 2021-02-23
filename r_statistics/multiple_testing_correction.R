###testing and multiple testing correction###

logcounts <- read.csv("data/logcounts.csv", row.names = 1)
View(logcounts)

cell_metadata <- read.csv("data/cell_metadata.csv", row.names = 1)
View(cell_metadata)

#cell_metadata <- t(cell_metadata)


#logcounts <- t(logcounts)
View(logcounts)

#Check if the names of the rows match before combining them into one dataframe
row.names(logcounts)== row.names(cell_metadata)
cell_names <- row.names(logcounts)
#reorder cell metadata to match logcount data
cell_metadata <- cell_metadata[cell_names,]

data.combined <- cbind(Infection= cell_metadata, as.data.frame(logcounts))
View(data.combined)

wilcox.test(ENSG00000131203 ~ Infection, data = data.combined)
t.test(ENSG00000131203 ~ Infection, data = data.combined)

logcounts= as.matrix(logcounts)
View(logcounts)

test_row <- function(index, matrix) {
  test_data <- data.frame(
    value = as.numeric(matrix[index, ]),
    group = cell_metadata$Infection)
  out <- wilcox.test(value ~ group, test_data)
  out$p.value}

x <-  test_row(1, logcounts)
str(x)

#define a list tat the function will be applied to
rowselect <- seq(1, nrow(logcounts),1)
rowselect

#apply the function to iterate rows in our logcount file
#numeric(1) creates a cector of length of 1
p_values <- vapply(rowselect, test_row, FUN.VALUE = numeric(1), matrix=logcounts)
p_values

#visualise the p-values
hist(p_values)

#adjust the p-values to the number of the tests performed
p_adjusted <- p.adjust(p_values, method= "BY")
hist(p_adjusted)

plot(p_values, p_adjusted)
abline(a=0, b=1)
abline(a=0.05, b=0)
abline(v=0.05)
