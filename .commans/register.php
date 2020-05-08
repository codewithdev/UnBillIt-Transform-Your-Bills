<? php ?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Untitled</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/Registration-Form-with-Photo.css">
    <link rel="stylesheet" href="assets/css/styles.css">
</head>

<body>
    <div class="register-photo">
        <div class="form-container">
            <div class="image-holder" style="width: 263px;background-repeat: no-repeat;background-size: cover;background-position: bottom;"></div>
            <form method="post">
                <h2 class="text-center"><strong>Create</strong> an account.
                 <button onclick="window.open('../home.php');window.close();" style="color: #000; text-decoration: none; float: right;font-size: inherit;font-weight: 700;text-shadow: 0 1px 0 #fff; opacity: 0.5; margin: 0;font-family: inherit;font-size: inherit;line-height: inherit;">
            <span area-hidden="true">&times</span>
        </button></h2>
                <div class="form-group"><input class="form-control" type="email" name="email" placeholder="Email"></div>
                <div class="form-group"><input class="form-control" type="password" name="password" placeholder="Password"></div>
                <div class="form-group"><input class="form-control" type="password" name="password-repeat" placeholder="Password (repeat)"></div>
                <div class="form-group">
                    <div class="form-check"><label class="form-check-label"><input class="form-check-input" type="checkbox">I agree to the license terms.</label></div>
                </div>
                <div class="form-group"><button class="btn btn-primary btn-block" type="submit">Sign Up</button></div><a class="already" href="index.php">You already have an account? Login here.</a></form>
        </div>
    </div>

    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
   
</body>

</html>