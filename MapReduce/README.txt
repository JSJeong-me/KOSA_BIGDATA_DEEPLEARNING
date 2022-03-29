mrjob fully supports Amazon's Elastic MapReduce (EMR) service, which allows you to buy time on a Hadoop cluster on an hourly basis. mrjob has basic support for Google Cloud Dataproc (Dataproc) which allows you to buy time on a Hadoop cluster on a minute-by-minute basis. It also works with your own Hadoop cluster.

Some important features:

Run jobs on EMR, Google Cloud Dataproc, your own Hadoop cluster, or locally (for testing).
Write multi-step jobs (one map-reduce step feeds into the next)
Easily launch Spark jobs on EMR or your own Hadoop cluster
Duplicate your production environment inside Hadoop
Upload your source tree and put it in your job's $PYTHONPATH
Run make and other setup scripts
Set environment variables (e.g. $TZ)
Easily install python packages from tarballs (EMR only)
Setup handled transparently by mrjob.conf config file
Automatically interpret error logs
SSH tunnel to hadoop job tracker (EMR only)
Minimal setup
To run on EMR, set $AWS_ACCESS_KEY_ID and $AWS_SECRET_ACCESS_KEY
To run on Dataproc, set $GOOGLE_APPLICATION_CREDENTIALS
No setup needed to use mrjob on your own Hadoop cluster