library(rPython)

# Global variables can go here
data <- read.table('./data/transfac.txt',header=T)
df <- 10

# Define the UI
ui <- bootstrapPage(
  selectInput(
    "script", "Choose script:",
    c("ATGs"="get_ATGs", "Fin anno"="get_fin_anno", "Promoters"="get_promoters")
  ),
  actionButton('run', 'Run script'),
  hr(),
  conditionalPanel(
    condition="input.script=='get_ATGs'",
    numericInput('df', 'Approximation', df)
  ),
  plotOutput('plot'),
  verbatimTextOutput('out1')
)

# Define the server code
server <- function(input, output) {
  output$out1 <- renderPrint({
    observeEvent(input$run, {
      system(paste('python ../Arabidopsis/', input$script, '.py ../Arabidopsis/data/TAIR10_GFF3_genes.gff', sep=''))
    })
  })
  output$plot <- renderPlot({
    if (input$script == 'get_ATGs') {
      plot(data,
        main="Transcription Factor Binding Sites (TRANSFAC database)",
        ylab='Fraction of promoters with TFBS',
        xlab='Distance from TSS, nt')
      lines(predict(smooth.spline(data,df=input$df)),col='red',lwd=3)
      abline(v=0)
    } else {
      plot(data)
    }
  })
}

# Return a Shiny app object
shinyApp(ui = ui, server = server)