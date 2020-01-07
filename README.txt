This builds a Lambda@Edge function that blows away an S3 object (fronted by non-caching CloudFront) as soon as it's read.

Handy for sensitive things that you don't want hanging around after the recipient sees it the first time.
