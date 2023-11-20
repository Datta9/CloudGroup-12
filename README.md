# CloudGroup-12
Create a repository in any source code management tool (preferably GitHub) , with a ReadMe file with table of contents of your project, and provide responses to all the questions below:


o Project Scope:
            Specific Problem: The project will aim to predict and understand factors influencing passenger satisfaction.This will align with educational goals related to machine learning and data analytics with practical applications in customer service and business strategy.

o Domain:   
            Industry: The project will be situated within the airline industry.
            Stakeholders: Stakeholders will include passengers, airline companies, regulatory bodies, and service providers within the airports.

Literature Review: Conduct a literature review of research papers, case
studies, articles, and books related to the chosen domain. The purpose is
to stay informed about the latest advancements and best practices in the
field. Sources should be current and at least 5 sources should be
documented and summarized.

Data Source(s): 
The below are the potential datasources from where we can gather features required for determining the satisfaction of the customer.
1. Airline Passenger Satisfaction | Kaggle: This dataset on Kaggle contains customer satisfaction scores from airline passengers.
2. Airlines - The American Customer Satisfaction Index: The American Customer Satisfaction Index provides a definitive measure of passenger satisfaction with cause-and-effect analysis. It includes data from 9 major airlines, plus an aggregate of smaller carriers. The 2023 results are based on data collected from April 2022 to March 2023.

3. Maven Churn Challenge | Maven Analytics: This dataset includes airline satisfaction scores for 129,880 passengers. Each record represents  one passenger and contains details about passenger demographics, flight distance and delays, travel class and purpose, and ratings for factors like cleanliness, comfort, and service, as well as overall satisfaction with the airline.

(1) Airline Passenger Satisfaction | Kaggle. https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction.

(2) Airline Passenger Satisfaction | Kaggle. https://www.kaggle.com/datasets/mysarahmadbhat/airline-passenger-satisfaction

(3)Airline Passenger Satisfaction | Kaggle. https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction.

(4) Airlines - The American Customer Satisfaction Index. https://theacsi.org/industries/travel/airlines/.   

(5) Airlines - The American Customer Satisfaction Index. https://theacsi.org/industries/travel/airlines/.

(6) Maven Churn Challenge | Maven Analytics. https://mavenanalytics.io/blog/maven-airlines-challenge.

(7) Maven Churn Challenge | Maven Analytics. https://mavenanalytics.io/blog/maven-airlines-challenge.

Domain-specific Challenges: 

Data Integration: Integrating data from different sources like customer feedback surveys, social media sentiment analysis, operational flight data, and third-party service ratings can be challenging due to the heterogeneity of data. Each source may have its own format, structure, and quality, requiring significant preprocessing and cleaning efforts.

Privacy Concerns: Collecting and analyzing data related to airline passenger satisfaction may involve handling sensitive personal information. Ensuring the privacy and anonymity of individuals while maintaining the utility of the data can be a significant challenge.

Real-Time Analysis: The need for real-time analysis can pose a challenge, especially when dealing with large volumes of data or when the data is streaming in nature, such as social media sentiment analysis.

Data Quality: The quality of data collected from sources like social media or customer feedback surveys can vary greatly. Issues such as bias in responses, missing data, or inaccurate data can impact the reliability of the analysis.


KPI’s: 
Key Performance Indicators (KPIs) in this context would encompass the utilization of data attributes, the extent of data preprocessing, and the diversity of the dataset. It's crucial to have a wide-ranging dataset for robust analysis. Another significant KPI involves experimenting with various machine learning algorithms to identify the one that delivers the best performance. The optimal model would be the one that most accurately predicts or classifies according to the problem at hand. These KPIs collectively contribute to the successful analysis of airline passenger satisfaction.

**DELIVERABLE - 2**

The dataset is centered on airline passenger satisfaction, encompassing a range of attributes such as gender, age, customer type, travel class, and flight distance. It differentiates types of travel into personal and business categories. The dataset offers detailed ratings for various services, including inflight wifi, seat comfort, food and drink, and cleanliness. Additionally, it provides ratings for specific services like inflight entertainment, on-board service, leg room service, baggage handling, check-in service, and inflight service, presenting a comprehensive view of the passenger's travel experience.

Flight delays are recorded in terms of departure and arrival delay minutes, shedding light on their impact on passenger satisfaction. The overall satisfaction level of passengers is categorized as either 'satisfied' or 'neutral or dissatisfied'. This data is crucial for airlines to analyze and predict factors influencing passenger satisfaction, making it an essential tool for market research, customer experience management, and service quality improvement in the aviation industry. The dataset's comprehensive nature makes it invaluable for understanding passenger preferences and improving airline services.

**Data Understanding**

We employed AWS Glue for schema discovery and data type definition, ensuring our dataset's structure was accurately recognized and categorized. Then we used Glue crawler for refining the dataset schema, allowing for precise categorization and organization of data fields. For in-depth querying and extracting insights, AWS Athena was used. This enabled us to perform comprehensive data analysis efficiently, allowing for complex queries and data aggregations.This approach not only streamlined our data analysis process but also enhanced the accuracy and relevance of the insights gained, proving crucial for informed decision-making and strategic planning Additionally, we utilized AWS QuickSight for data visualization. QuickSight's powerful visualization tools provided an intuitive interface for exploring and presenting the data, making it easier to identify patterns, trends, and correlations. This visual approach to data analysis enhanced our ability to gain insights, allowing us to make more informed decisions and develop effective strategies based on the dataset.

**AWS GLUE**

 ![Glue pipline ](https://github.com/Datta9/CloudGroup-12/assets/116744004/89c16af9-f4ba-4944-8202-fc9fbc26b445)
 
![glue schema](https://github.com/Datta9/CloudGroup-12/assets/116744004/0aa587d9-e8b0-4e8d-b018-90c960081976)

**AWS ATHENA**
<img width="1440" alt="Query1" src="https://github.com/Datta9/CloudGroup-12/assets/116744004/b6ca58ce-5cdb-4587-91a0-c58ba4f3e7b1">

<img width="1440" alt="Query2" src="https://github.com/Datta9/CloudGroup-12/assets/116744004/bca5ff38-45b6-4fb7-ab48-9d854e708820">

<img width="1440" alt="Query3" src="https://github.com/Datta9/CloudGroup-12/assets/116744004/d356b7c6-1309-4f2b-aaca-01946e0db61d">

<img width="1440" alt="Query4" src="https://github.com/Datta9/CloudGroup-12/assets/116744004/40c46523-1e7f-410d-9d42-dac68898634a">

<img width="1440" alt="Query5" src="https://github.com/Datta9/CloudGroup-12/assets/116744004/3c318720-0012-45aa-bab5-075c0e339d7c">

**AWS QUICKSITE**
![visualization](https://github.com/Datta9/CloudGroup-12/assets/116744004/fe47f0f7-b3b3-418a-b658-7593043d29ce)

![visualization 2](https://github.com/Datta9/CloudGroup-12/assets/116744004/b992a738-122d-4eed-82c4-dfa055edcea5)






