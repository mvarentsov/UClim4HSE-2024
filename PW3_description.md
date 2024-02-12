# Практическая работа №1. Анализ данных мониторинга и моделирования для городов

### Часть 1. Анализ данных мезомоделирования
* Необходим выбрать один из городов, для которых в Copernicus Data Store доступны данные [“Climate variables for cities in Europe from 2008 to 2017”](https://cds.climate.copernicus.eu/cdsapp#!/dataset/sis-urban-climate-cities?tab=form)
  ![image](https://github.com/mvarentsov/Urban-climate-modelling4HSE/assets/67764064/74eb513e-7778-4606-b0db-f9763cb2ec98)

* Скачать данные по всем переменным за 1 месяц 
* Скачать данные реанализа ERA5 для города и его окрестностей за этот же месяц
* **To be continued …**

**Справка:** анализируемые данные полученны с в результате динамического даунскейлинга реанализа ERA5 с использованим модели пограничного слоя UrbClim [(de Ridder et al., 2015)](https://www.sciencedirect.com/science/article/abs/pii/S2212095515000024).
![image](https://github.com/mvarentsov/Urban-climate-modelling4HSE/assets/67764064/9047f526-7f42-42d8-ae86-76b5c52a40f9)


### Часть 2. Работа с моделью городского полога 
* Необходим запустить скрипт сборки и запуска модели TEB [PW3_ERA5_to_TEB.ipynb](https://github.com/mvarentsov/Urban-climate-modelling4HSE/blob/main/Practice/PW3_ERA5_to_TEB.ipynb) в Google Colab с использованием доступных по умолчанию данных для Москвы, убедиться в его штатной работе. 
* На основе скачанных ранее данных ERA5 подготовить входные данные (метеорологический форсинг) для модели TEB для вашего города, используя скрипт [PW3_ERA5_to_TEB.ipynb](https://github.com/mvarentsov/Urban-climate-modelling4HSE/blob/main/Practice/PW3_ERA5_to_TEB.ipynb)
* Попробовать заменить данные для Москвы данными для вашего города, посмотреть что получится
* **To be continued …**

**Справка:** модель гордского полога (гордского каньона) TEB (Town Energy Ballance) - первая из городских параметризаций [(Masson, 2000)](https://link.springer.com/article/10.1023/A:1002463829265). В рамках задания предпологается запускать модель TEB в оффлайн режиме, т.е. когда характеристики атмосферы над городом задаются в качестве форсинга. 

![image](https://github.com/mvarentsov/Urban-climate-modelling4HSE/assets/67764064/cc7b3819-369d-41f6-a9b0-13e7e58e712e)

  
