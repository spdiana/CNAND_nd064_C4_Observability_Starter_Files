**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*1* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and
include it here to verify the installation

Images in the `answer-img` directory: ks8_***.png


## Setup the Jaeger and Prometheus source
*2* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

Image in the `answer-img` directory: grafana1.png, grafana2.png


## Create a Basic Dashboard
*3* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

Image in the `answer-img` directory: prometheus_grafana_dashboard.png


## Describe SLO/SLI
*4* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

Service level indicators (SLIs) and Service Level Objectives (SLOs) are metrics to help "Site reliability engineering" measure
and define metrics towards applications/services to reach and monitor measurable goal over a period of time. An SLI measures compliance with an SLO.
Choosing the right metrics helps drive the right action if something goes wrong and also gives an SRE team confidence that a service is healthy.
There's a third metric SLA (Service Level Agreement) that the business team will sign with customers.
SLA is the promise, SLO is the goal, SLI how was/is going/did.

*monthly uptime*  
If SLA specifies the systems or service *monthly uptime* or *month availability* will be available 99.95% of the time,
the SLO will likely be 99.95% uptime and the SLI is the real/actual measurement of your uptime. Maybe it’s 99.96%. Maybe 99.99%.

*request response time*  
Request response time is the duration of a transaction from the perspective of the requester.
If SLA specifies the systems or service for every additional .1% of HTTP 500s, 5% refund of total contract.
the SLO will likely be less 1% HTTP 500s over 30 days and the SLI indicator is HTTP status codes

References:  
https://www.atlassian.com/incident-management/kpis/sla-vs-slo-vs-sli  
https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring  
https://epsagon.com/development/slas-slos-slis-guide/  
https://docs.newrelic.com/docs/new-relic-solutions/new-relic-solutions/measure-devops-success/establish-objectives-baselines-define-team-slos/

## Creating SLI metrics.
*5* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

Latency  
The proportion of requests that were faster than some threshold, indicates whether the service is fast enough.
It can measure latency by calculating the difference between when a timer starts and when it stops for a given request type.
How long does it take to read and write data?  How long did it take to respond?

Throughput  
The proportion of time where the data processing rate was faster than a threshold in certain period of time.
Can be used to measure the performance of hard drives and RAM, as well as Internet and network connections
How many requests were you able to handle?

Availability  
The proportion of requests that resulted in a successful response. To measure the availability of a service, could subtract
the amount of downtime from the Agreed Service Time.
Were you able respond to the request? Could the server respond to the request successfully? Can the data be accessed on demand?
How many requests have returned successfully?

Error rate
The number of errors during a fixed period exceeds a threshold. The metrics capture the number of erroneous results, usually
expressed as a rate of errors per unit time or some other unit of work.
How many errors were generated for the request that was handled?

Freshness
The metric that measures the “recency” of the information accessed by the user.

References:  
https://www.ibm.com/garage/method/practices/manage/service-level-objective/
https://www.bmc.com/blogs/service-level-indicator-metrics/#
https://sre.google/workbook/implementing-slos/
https://cloud.google.com/architecture/adopting-slos

## Create a Dashboard to measure our SLIs
*6:* Create a dashboard to measure the uptime of the frontend and backend services. We will also want to measure 40x and 50x errors.
Create a dashboard that show these values over a 24 hour period and take a screenshot.

Image in the `answer-img` directory: up_time.png
Image in the `answer-img` directory: http_errors_backend.png/http_errors_frontend.png

## Tracing our Flask App
*7:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.
Image in the `answer-img` directory: jaeger.png

## Jaeger in Dashboards
*8:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
Image in the `answer-img` directory: jaeger_grafana.png

## Report Error
*9:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and
to let them know the file that is causing the issue.

TROUBLE TICKET

Name: backend service issue on pod

Date: 30/10/2021

Subject: connection pool is exhausted

Affected Area: customer service

Severity: High

Description:  Incident at 30/10/2021 19:00hs, it was discovered that one pod had the connection pool exhausted, 
resulting in failed check customer status, getting 500 error.


## Creating SLIs and SLOs
*10:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure
the success of this SLO.

## Building KPIs for our plan
*11*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write
them down here.

## Final Dashboard
*12*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a
screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
