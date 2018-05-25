library(rPython)

# Global variables can go here
data <- read.table('./data/transfac.txt',header=T)
df <- 10

# Define the UI
ui <- bootstrapPage(
  actionButton('run', 'Run script'),
  verbatimTextOutput('out1'),
  numericInput('df', 'Number of obs', df),
  plotOutput('plot')
)


# Define the server code
server <- function(input, output) {
  output$out1 <- renderPrint({
    observeEvent(input$run, {
      system('python ../Arabidopsis/get_ATGs.py ../Arabidopsis/data/TAIR10_GFF3_genes.gff')
    })
  })
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