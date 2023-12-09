/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
  async function getList() {
    try {
      const response = await fetch('http://127.0.0.1:5000/get_predictions');
      
      if (!response.ok) {
        console.log(response);
        alert('Ocorreu um erro ao trazer as predições!');
      }

      const data = await response.json();
      data?.predictions?.forEach(item => insertList(item.name, item.male === 1 ? 'M' : 'F', item.age, item.education, transformInputYesOrNo(item.current_smoker), item.cigs_per_day, transformInputYesOrNo(item.bp_meds), transformInputYesOrNo(item.prevalent_stroke), transformInputYesOrNo(item.prevalent_hyp), transformInputYesOrNo(item.diabetes), item.tot_chol, item.sys_bp, item.dia_bp, item.bmi, item.heart_rate, item.glucose, item.ten_year_chd === 1 ? 'Há Risco' : 'Não há risco'))
    } catch (error) {
      console.error('Error:', error);
    }
  }

  /*
    --------------------------------------------------------------------------------------
    Chamada da função para carregamento inicial dos dados
    --------------------------------------------------------------------------------------
  */
  getList()
  
  /*
    --------------------------------------------------------------------------------------
    Função para colocar um item na lista do servidor via requisição POST
    --------------------------------------------------------------------------------------
  */
  const postItem = async (inputPatientName, inputGender, inputAge, inputEducation, inputSmoker, inputCigarsDay, inputMedPres, inputPrevalentStroke, inputPrevalentHyp, inputDiabetes, inputCholesterol, inputSysBP, inputDiaBP, inputBmi, inputHeartRate, inputGlucose) => {
      const formData = new FormData();
      formData.append('name', inputPatientName);
      formData.append('male', inputGender);
      formData.append('age', inputAge);
      formData.append('education', inputEducation);
      formData.append('current_smoker', inputSmoker);
      formData.append('cigs_per_day', inputCigarsDay);
      formData.append('bp_meds', inputMedPres);
      formData.append('prevalent_stroke', inputPrevalentStroke);
      formData.append('prevalent_hyp', inputPrevalentHyp);
      formData.append('diabetes', inputDiabetes);
      formData.append('tot_chol', inputCholesterol);
      formData.append('sys_bp', inputSysBP);
      formData.append('dia_bp', inputDiaBP);
      formData.append('bmi', inputBmi);
      formData.append('heart_rate', inputHeartRate);
      formData.append('glucose', inputGlucose);
  
    fetch('http://127.0.0.1:5000/add_prediction', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    alert('Predição adicionada com sucesso');
    location.reload()
    getList()
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para criar um botão close para cada item da lista
    --------------------------------------------------------------------------------------
  */
  const insertButton = (parent) => {
    let span = document.createElement('span');
    let txt = document.createTextNode('\u00D7');
    span.className = 'close';
    span.appendChild(txt);
    parent.appendChild(span);
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para remover um item da lista de acordo com o click no botão close
    --------------------------------------------------------------------------------------
  */
  const removeElement = () => {
    let close = document.getElementsByClassName('close');
    let i;
    for (i = 0; i < close.length; i++) {
      close[i].onclick = function () {
        let div = this.parentElement.parentElement;
        const nameItem = div.getElementsByTagName('td')[0].innerHTML
        if (confirm('Você tem certeza?')) {
          div.remove()
          deleteItem(nameItem)
          alert('Removido!')
        }
      }
    }
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para deletar um item da lista do servidor via requisição DELETE
    --------------------------------------------------------------------------------------
  */

  const deleteItem = (item) => {
    console.log(item)
    let url = 'http://127.0.0.1:5000/del_prediction?name=' + item;
    fetch(url, {
      method: 'DELETE'
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para adicionar um novo item com nome, quantidade e valor 
    --------------------------------------------------------------------------------------
  */
  const newItem = () => {
    const regexGender = /[MF]/;
    const regex = /[SN]/;
    let inputPatientName = document.getElementById('patientName').value;
    let inputGender = document.getElementById('gender').value.toUpperCase();
    let inputAge = document.getElementById('age').value;
    let inputEducation = document.getElementById('education').value;
    let inputSmoker = document.getElementById('smoker').value.toUpperCase();
    let inputCigarsDay = document.getElementById('cigarsDay').value;
    let inputMedPres = document.getElementById('medPres').value.toUpperCase();
    let inputPrevalentStroke = document.getElementById('prevalentStroke').value.toUpperCase();
    let inputPrevalentHyp = document.getElementById('prevalentHyp').value.toUpperCase();
    let inputDiabetes = document.getElementById('diabetes').value.toUpperCase();
    let inputCholesterol = document.getElementById('cholesterol').value;
    let inputSysBP = document.getElementById('sysBP').value;
    let inputDiaBP = document.getElementById('diaBP').value;
    let inputBmi = document.getElementById('bmi').value;
    let inputHeartRate = document.getElementById('heartRate').value;
    let inputGlucose = document.getElementById('glucose').value;

    if (inputPatientName === '') {
      alert('O campo Nome do paciente não pode ser vazio');
    } else if (!regexGender.test(inputGender)) {
      alert('Favor colocar o sexo biológico: M para masculino e F para feminino');
    } else if (!regex.test(inputSmoker)) {
      alert('O campo Fumante precisa ser preenchido com S para sim ou N para não.');
    } else if (!regex.test(inputMedPres)) {
      alert('O campo Remédio pressão precisa ser preenchido com S para sim ou N para não.');
    } else if (!regex.test(inputPrevalentStroke)) {
      alert('O campo Já enfartou precisa ser preenchido com S para sim ou N para não.');
    } else if (!regex.test(inputPrevalentHyp)) {
      alert('O campo Hipertensão precisa ser preenchido com S para sim ou N para não.');
    } else if (!regex.test(inputDiabetes)) {
      alert('O campo Diabetes precisa ser preenchido com S para sim ou N para não.');
    } else {
      inputGender = inputGender === 'M' ? 1 : 0;
      inputSmoker = transformInputYesOrNo(inputSmoker);
      inputMedPres = transformInputYesOrNo(inputMedPres);
      inputPrevalentStroke = transformInputYesOrNo(inputPrevalentStroke);
      inputPrevalentHyp = transformInputYesOrNo(inputPrevalentHyp);
      inputDiabetes = transformInputYesOrNo(inputDiabetes);

      postItem(inputPatientName, inputGender, inputAge, inputEducation, inputSmoker, inputCigarsDay, inputMedPres, inputPrevalentStroke, inputPrevalentHyp, inputDiabetes, inputCholesterol, inputSysBP, inputDiaBP, inputBmi, inputHeartRate, inputGlucose);
    }
  }

  /*
    --------------------------------------------------------------------------------------
    Função para transformar o valor de um input em um valor utilizável.
    --------------------------------------------------------------------------------------
  */
  const transformInputYesOrNo = (inputValue) => {
    if (typeof inputValue === 'string') {
      return inputValue === 'S' ? 1 : 0;
    }
    if (typeof inputValue === 'number') {
      return inputValue === 1 ? 'S' : 'N';
    }
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para inserir items na lista apresentada
    --------------------------------------------------------------------------------------
  */
  const insertList = (name, male, age, education, current_smoker, cigs_per_day, bp_meds, prevalent_stroke, prevalent_hyp, diabetes, tot_chol, sys_bp, dia_bp, bmi, heart_rate, glucose, ten_year_chd) => {
    var item = [name, male, age, education, current_smoker, cigs_per_day, bp_meds, prevalent_stroke, prevalent_hyp, diabetes, tot_chol, sys_bp, dia_bp, bmi, heart_rate, glucose, ten_year_chd]
    var table = document.getElementById('myTable');
    var row = table.insertRow();
  
    for (var i = 0; i < item.length; i++) {
      var cel = row.insertCell(i);
      cel.textContent = item[i];
    }
    insertButton(row.insertCell(-1))
    document.getElementById('patientName').value = '';
    document.getElementById('gender').value = '';
    document.getElementById('age').value = '';
    document.getElementById('education').value = '';
    document.getElementById('smoker').value = '';
    document.getElementById('cigarsDay').value = '';
    document.getElementById('medPres').value = '';
    document.getElementById('prevalentStroke').value = '';
    document.getElementById('prevalentHyp').value = '';
    document.getElementById('diabetes').value = '';
    document.getElementById('cholesterol').value = '';
    document.getElementById('sysBP').value = '';
    document.getElementById('diaBP').value = '';
    document.getElementById('bmi').value = '';
    document.getElementById('heartRate').value = '';
    document.getElementById('glucose').value = '';
  
    removeElement()
  }
