var url = 'http://127.0.0.1:8000/api/v1/'
  
var apiUrl1 = url + 'AtPiezas';
var apiUrl2 = url + 'materiales';
var apiUrl3 = url + 'AtModelos';
var apiUrl4 = url + 'empleados';

chartColor = "#FFFFFF";

gradientChartOptionsConfiguration = {
  maintainAspectRatio: false,
  legend: {
    display: false
  },
  tooltips: {
    bodySpacing: 4,
    mode: "nearest",
    intersect: 0,
    position: "nearest",
    xPadding: 10,
    yPadding: 10,
    caretPadding: 10
  },
  responsive: 1,
  scales: {
    yAxes: [{
      display: 0,
      gridLines: 0,
      ticks: {
        display: false
      },
      gridLines: {
        zeroLineColor: "transparent",
        drawTicks: false,
        display: false,
        drawBorder: false
      }
    }],
    xAxes: [{
      display: 0,
      gridLines: 0,
      ticks: {
        display: false
      },
      gridLines: {
        zeroLineColor: "transparent",
        drawTicks: false,
        display: false,
        drawBorder: false
      }
    }]
  },
  layout: {
    padding: {
      left: 0,
      right: 0,
      top: 15,
      bottom: 15
    }
  }
};

gradientChartOptionsConfigurationWithNumbersAndGrid = {
  maintainAspectRatio: false,
  legend: {
    display: false
  },
  tooltips: {
    bodySpacing: 4,
    mode: "nearest",
    intersect: 0,
    position: "nearest",
    xPadding: 10,
    yPadding: 10,
    caretPadding: 10
  },
  responsive: true,
  scales: {
    yAxes: [{
      gridLines: 0,
      gridLines: {
        zeroLineColor: "transparent",
        drawBorder: false
      }
    }],
    xAxes: [{
      display: 0,
      gridLines: 0,
      ticks: {
        display: false
      },
      gridLines: {
        zeroLineColor: "transparent",
        drawTicks: false,
        display: false,
        drawBorder: false
      }
    }]
  },
  layout: {
    padding: {
      left: 0,
      right: 0,
      top: 15,
      bottom: 15
    }
  }
};
  
// Grafica Principal
fetch(apiUrl3)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.modelo.nombre);
    data.push(dato.cantidad);
  });


  var ctx = document.getElementById('PrincipalGrafica').getContext("2d");

  var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
  gradientStroke.addColorStop(0, '#80b6f4');
  gradientStroke.addColorStop(1, chartColor);

  var gradientFill = ctx.createLinearGradient(0, 200, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, "rgba(255, 255, 255, 0.24)");

  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: "Cantidad de Modelos Producidos",
        borderColor: chartColor,
        pointBorderColor: chartColor,
        pointBackgroundColor: "#1e3d60",
        pointHoverBackgroundColor: "#1e3d60",
        pointHoverBorderColor: chartColor,
        pointBorderWidth: 1,
        pointHoverRadius: 7,
        pointHoverBorderWidth: 2,
        pointRadius: 5,
        fill: true,
        backgroundColor: gradientFill,
        borderWidth: 2,
        data: data
      }]
    },
    options: {
      layout: {
        padding: {
          left: 20,
          right: 20,
          top: 0,
          bottom: 0
        }
      },
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: '#fff',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      legend: {
        position: "bottom",
        fillStyle: "#FFF",
        display: false
      },
      scales: {
        yAxes: [{
          ticks: {
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold",
            beginAtZero: true,
            maxTicksLimit: 5,
            padding: 10
          },
          gridLines: {
            drawTicks: true,
            drawBorder: false,
            display: true,
            color: "rgba(255,255,255,0.1)",
            zeroLineColor: "transparent"
          }

        }],
        xAxes: [{
          gridLines: {
            zeroLineColor: "transparent",
            display: false,

          },
          ticks: {
            padding: 10,
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold"
          }
        }]
      }
    }
  });         
  


  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});      
  


// Graficas Pagina Principal
var cardStatsMiniLineColor = "#fff",
cardStatsMiniDotColor = "#fff";
  
fetch(apiUrl1)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.pieza__nombre);
    data.push(dato.stock);
  });

  ctx = document.getElementById('Grafica2').getContext("2d");

  gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
  gradientStroke.addColorStop(0, '#80b6f4');
  gradientStroke.addColorStop(1, chartColor);
  
  gradientFill = ctx.createLinearGradient(0, 170, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, "rgba(249, 99, 59, 0.40)");
  
  var myChart = new Chart(ctx, {
  type: 'line',
  responsive: true,
  data: {
    labels: labels,
    datasets: [{
      label: "Cantidad",
      borderColor: "#f96332",
      pointBorderColor: "#FFF",
      pointBackgroundColor: "#f96332",
      pointBorderWidth: 2,
      pointHoverRadius: 4,
      pointHoverBorderWidth: 1,
      pointRadius: 4,
      fill: true,
      backgroundColor: gradientFill,
      borderWidth: 2,
      data: data
    }]
  },
  options: gradientChartOptionsConfiguration
  });


  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});
  
fetch(apiUrl2)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.nombre);
    data.push(dato.stock);
  });

  ctx = document.getElementById('Grafica3').getContext("2d");

  gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
  gradientStroke.addColorStop(0, '#18ce0f');
  gradientStroke.addColorStop(1, chartColor);
  
  gradientFill = ctx.createLinearGradient(0, 170, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, hexToRGB('#18ce0f', 0.4));
  
  var myChart = new Chart(ctx, {
  type: 'line',
  responsive: true,
  data: {
    labels: labels,
    datasets: [{
      label: "Cantidad",
      borderColor: "#18ce0f",
      pointBorderColor: "#FFF",
      pointBackgroundColor: "#18ce0f",
      pointBorderWidth: 2,
      pointHoverRadius: 4,
      pointHoverBorderWidth: 1,
      pointRadius: 4,
      fill: true,
      backgroundColor: gradientFill,
      borderWidth: 2,
      data: data
    }]
  },
  options: gradientChartOptionsConfigurationWithNumbersAndGrid
  });

  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});

fetch(apiUrl4)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.areatrabajo__nombre);
    data.push(dato.empleados);
  });

  var ctx = document.getElementById("Grafica4").getContext("2d");

  gradientFill = ctx.createLinearGradient(0, 170, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, hexToRGB('#2CA8FF', 0.6));
  
  var a = {
  type: "line",
  data: {
    labels: labels,
    datasets: [{
      label: "Cantidad de Empleados",
      backgroundColor: gradientFill,
      borderColor: "#2CA8FF",
      pointBorderColor: "#FFF",
      pointBackgroundColor: "#2CA8FF",
      pointBorderWidth: 2,
      pointHoverRadius: 4,
      pointHoverBorderWidth: 1,
      pointRadius: 4,
      fill: true,
      borderWidth: 1,
      data: data
    }]
  },
  options: {
    maintainAspectRatio: false,
    legend: {
      display: false
    },
    tooltips: {
      bodySpacing: 4,
      mode: "nearest",
      intersect: 0,
      position: "nearest",
      xPadding: 10,
      yPadding: 10,
      caretPadding: 10
    },
    responsive: 1,
    scales: {
      yAxes: [{
        gridLines: 0,
        gridLines: {
          zeroLineColor: "transparent",
          drawBorder: false
        }
      }],
      xAxes: [{
        display: 0,
        gridLines: 0,
        ticks: {
          display: false
        },
        gridLines: {
          zeroLineColor: "transparent",
          drawTicks: false,
          display: false,
          drawBorder: false
        }
      }]
    },
    layout: {
      padding: {
        left: 0,
        right: 0,
        top: 15,
        bottom: 15
      }
    }
  }
  };
  
  var viewsChart = new Chart(ctx, a);
    

  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});

// Grafica Areas de Trabajo Principal
fetch(apiUrl4)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.areatrabajo__nombre);
    data.push(dato.empleados);
  });


  var ctx = document.getElementById('GraficaCantidadEmpleados').getContext("2d");

  var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
  gradientStroke.addColorStop(0, '#80b6f4');
  gradientStroke.addColorStop(1, chartColor);

  var gradientFill = ctx.createLinearGradient(0, 200, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, "rgba(255, 255, 255, 0.24)");

  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: "Empleados",
        borderColor: chartColor,
        pointBorderColor: chartColor,
        pointBackgroundColor: "#1e3d60",
        pointHoverBackgroundColor: "#1e3d60",
        pointHoverBorderColor: chartColor,
        pointBorderWidth: 1,
        pointHoverRadius: 7,
        pointHoverBorderWidth: 2,
        pointRadius: 5,
        fill: true,
        backgroundColor: gradientFill,
        borderWidth: 2,
        data: data
      }]
    },
    options: {
      layout: {
        padding: {
          left: 20,
          right: 20,
          top: 0,
          bottom: 0
        }
      },
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: '#fff',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      legend: {
        position: "bottom",
        fillStyle: "#FFF",
        display: false
      },
      scales: {
        yAxes: [{
          ticks: {
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold",
            beginAtZero: true,
            maxTicksLimit: 5,
            padding: 10
          },
          gridLines: {
            drawTicks: true,
            drawBorder: false,
            display: true,
            color: "rgba(255,255,255,0.1)",
            zeroLineColor: "transparent"
          }

        }],
        xAxes: [{
          gridLines: {
            zeroLineColor: "transparent",
            display: false,

          },
          ticks: {
            padding: 10,
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold"
          }
        }]
      }
    }
  });         
  


  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});     

// Graficas de Crud

// Piezas
fetch(apiUrl1)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.nombre);
    data.push(dato.stock);
  });


  var ctx = document.getElementById('GraficaPiezas').getContext("2d");

  var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
  gradientStroke.addColorStop(0, '#80b6f4');
  gradientStroke.addColorStop(1, chartColor);

  var gradientFill = ctx.createLinearGradient(0, 200, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, "rgba(255, 255, 255, 0.24)");

  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: "Cantidad",
        borderColor: chartColor,
        pointBorderColor: chartColor,
        pointBackgroundColor: "#1e3d60",
        pointHoverBackgroundColor: "#1e3d60",
        pointHoverBorderColor: chartColor,
        pointBorderWidth: 1,
        pointHoverRadius: 7,
        pointHoverBorderWidth: 2,
        pointRadius: 5,
        fill: true,
        backgroundColor: gradientFill,
        borderWidth: 2,
        data: data
      }]
    },
    options: {
      layout: {
        padding: {
          left: 20,
          right: 20,
          top: 0,
          bottom: 0
        }
      },
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: '#fff',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      legend: {
        position: "bottom",
        fillStyle: "#FFF",
        display: false
      },
      scales: {
        yAxes: [{
          ticks: {
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold",
            beginAtZero: true,
            maxTicksLimit: 5,
            padding: 10
          },
          gridLines: {
            drawTicks: true,
            drawBorder: false,
            display: true,
            color: "rgba(255,255,255,0.1)",
            zeroLineColor: "transparent"
          }

        }],
        xAxes: [{
          gridLines: {
            zeroLineColor: "transparent",
            display: false,

          },
          ticks: {
            padding: 10,
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold"
          }
        }]
      }
    }
  });         
  


  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});

// Materiales
fetch(apiUrl2)
.then(response => {
  // Verificar si la respuesta es exitosa (código de estado 200)
  if (!response.ok) {
    throw new Error('Error en la solicitud');
  }

  // Parsear la respuesta como JSON
  return response.json();
})
.then(dataJson => {

  var datos = dataJson;

  // Crear arrays separados para cada propiedad
  var labels = [];
  var data = [];

  // Iterar sobre los datos y llenar los arrays
  datos.forEach(function(dato) {
    labels.push(dato.nombre);
    data.push(dato.stock);
  });


  var ctx = document.getElementById('GraficaMateriales').getContext("2d");

  var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
  gradientStroke.addColorStop(0, '#80b6f4');
  gradientStroke.addColorStop(1, chartColor);

  var gradientFill = ctx.createLinearGradient(0, 200, 0, 50);
  gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
  gradientFill.addColorStop(1, "rgba(255, 255, 255, 0.24)");

  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: "Cantidad",
        borderColor: chartColor,
        pointBorderColor: chartColor,
        pointBackgroundColor: "#1e3d60",
        pointHoverBackgroundColor: "#1e3d60",
        pointHoverBorderColor: chartColor,
        pointBorderWidth: 1,
        pointHoverRadius: 7,
        pointHoverBorderWidth: 2,
        pointRadius: 5,
        fill: true,
        backgroundColor: gradientFill,
        borderWidth: 2,
        data: data
      }]
    },
    options: {
      layout: {
        padding: {
          left: 20,
          right: 20,
          top: 0,
          bottom: 0
        }
      },
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: '#fff',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      legend: {
        position: "bottom",
        fillStyle: "#FFF",
        display: false
      },
      scales: {
        yAxes: [{
          ticks: {
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold",
            beginAtZero: true,
            maxTicksLimit: 5,
            padding: 10
          },
          gridLines: {
            drawTicks: true,
            drawBorder: false,
            display: true,
            color: "rgba(255,255,255,0.1)",
            zeroLineColor: "transparent"
          }

        }],
        xAxes: [{
          gridLines: {
            zeroLineColor: "transparent",
            display: false,

          },
          ticks: {
            padding: 10,
            fontColor: "rgba(255,255,255,0.4)",
            fontStyle: "bold"
          }
        }]
      }
    }
  });         
  


  // Aquí puedes realizar cualquier operación con los datos, como dividirlos en arrays, mostrarlos en la interfaz de usuario, etc.
})
.catch(error => {
  console.error('Error:', error);
});

