# Global variables can go here
data <- read.table('./data/transfac.txt',header=T)
df <- 10

# Define the UI
ui <- bootstrapPage(
  numericInput('df', 'Number of obs', df),
  plotOutput('plot')
)


# Define the server code
server <- function(input, output) {
  output$plot <- renderPlot({
    plot(data,
      main="Transcription Factor Binding Sites (TRANSFAC database)",
      ylab='Fraction of promoters with TFBS',
      xlab='Distance from TSS, nt')
    lines(predict(smooth.spline(data,df=input$df)),col='red',lwd=3)
    abline(v=0)
  })
}

# Return a Shiny app object
shinyApp(ui = ui, server = server)