# Flying CO2 Emittion Calculator

본 프로젝트는 `IB MYP Personal Project` 의 일환으로 시작한 간단한 프로젝트입니다.
This is a  project that was created as part of the `IB MYP Personal Project`.

`aviationCO2` 프로젝트는 비행 시간을 기준으로 다양한 항공기 유형에 대한 승객 1인당 연료 소비량과 CO2 배출량을 계산합니다. 이 도구는 항공 여행의 환경적 영향을 이해하는 데 도움이 됩니다.

The `aviationCO2` project calculates the fuel consumption and CO2 emissions per passenger for different aircraft types based on the flying time. This tool helps to understand the environmental impact of air travel.

## 요구사항 | Requirements
- 파이썬 버전 3.8 또는 그 이상 | Python 3.8 or higher

## 설치 방법 | Installation
1. 리포지토리 복제 | Clone the repository:
    ```sh
    git clone https://github.com/yourusername/aviationCO2.git
    cd aviationCO2
    ```

## 사용 방법 | Usage
1. 스크립트 실행 | Run the script:
    ```sh
    python aviationCO2.py
    ```

2. 메시지가 나타나면 비행 시간을 시간을 입력하세요. 스크립트는 다음 항공기 유형에 대한 승객당 연료 소비량과 CO2 배출량을 계산하고 표시합니다: | Enter the flying time in hours when prompted. The script will calculate and display the fuel consumption and CO2 emissions per passenger for the following aircraft types:
    - B737-800
    - A320-200
    - B787-9
    - B777-300ER

3. 각 항공기 유형별로 연소된 연료와 승객당 CO2 배출량을 보여주는 표 및 그래프 형식으로 정보를 리턴해줍니다.The output will be displayed in a table format showing the fuel burned and CO2 emissions per passenger for each aircraft type.

## 실 사용 예 | Example
```sh
Enter the time flying in hours: 5
Table: Fuel Burned and CO2 Emissions per Passenger for Different Aircrafts
----------------------------------------------------------------------
   Aircraft  |  Fuel (kg/passenger)  |  CO2 (kg/passenger)
----------------------------------------------------------------------
  B737-800   |  68.8                 |  217.4
  A320-200   |  67.5                 |  213.3
  B787-9     |  94.6                 |  298.9
  B777-300ER |  101.9                |  321.9
----------------------------------------------------------------------
