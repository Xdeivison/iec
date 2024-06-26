
async function getJSON(response) {
  if (response.status == 204) return '';
  return response.json();
}

function apiService(endpoint, method, data) {
  const config = {
      method: method || "GET",
      body: data !== undefined ? JSON.stringify(data) : null,
      headers: {
          'content-type': 'application/json',
          'X-CSRFTOKEN': CSRF_TOKEN
      }
  }
  return fetch(endpoint, config)
          .then(getJSON)
          .catch(error => console.log(error))
}

function Show_Chirps_Data(pixel, startDate, finalDate){
  startDay = startDate.slice(0, 2)
  startMonth = startDate.slice(3, 5)
  startYear = startDate.slice(6)

  finalDay = finalDate.slice(0, 2)
  finalMonth = finalDate.slice(3, 5)
  finalYear = finalDate.slice(6)

  startDate = startYear + "-" + startMonth + "-" + startDay
  finalDate = finalYear + "-" + finalMonth + "-" + finalDay

  pixel_data = {
    "latitude": pixel.properties.latitude,
    "longitude": pixel.properties.longitude,
    "resolution": 0.05,
    "data_model_name": "Chirps",
    "startDate": startDate, // YYYY-MM-DD
    "finalDate": finalDate, // YYYY-MM-DD
  }

  $.getJSON(url_api, pixel_data, function(data) {
    var variable = 'evapo';
    switch (selBox_variable_display.value.toLowerCase()) {
      case 'evapotranspiração':
        variable = 'evapo'
        break;
      case 'temperatura mínima':
        variable = "minTemp";
        break;
      case 'temperatura máxima':
        variable = "maxTemp";
        break;
      case 'radiação de onda curta incidente à superficie':
        variable = 'ocis';
        break;
      case 'precipitação':
        variable = 'precip';
        break;
      case 'escoamento superficial':
        variable = 'rnof';
        break;
      case 'temperatura a 2m da superfície':
        variable = 'tp2m';
        break;
      default:
        variable = 'evapo';
        break;
    }
    chart_update2(chart, data, variable);
  })
}
  
  function Download_Chirps_Data(pixel_id, startDate, finalDate){
    startDay = startDate.slice(0, 2)
    startMonth = startDate.slice(3, 5)
    startYear = startDate.slice(6)
  
    finalDay = finalDate.slice(0, 2)
    finalMonth = finalDate.slice(3, 5)
    finalYear = finalDate.slice(6)
  
    startDate = startYear + "-" + startMonth + "-" + startDay
    finalDate = finalYear + "-" + finalMonth + "-" + finalDay
  
    pixel_data = {
      "latitude": pixel.properties.latitude,
      "longitude": pixel.properties.longitude,
      "resolution": 0.05,
      "data_model_name": "Chirps",
      "startDate": startDate, // YYYY-MM-DD
      "finalDate": finalDate, // YYYY-MM-DD
      "data_format": "csv"
    }
  
    var url = url_pixels + "csv/" + pixel_id + "/" + selBox_model_display.value + "/" +startDate + "/" + finalDate;
    var url = url_api + 

    $.ajax({
        url: url_api,
        type: 'GET',
        data: pixel_data,
        success: function(response) {
            console.log(response);
            window.location = url_api;
        }
    });

    window.location.href = url;
  }
  