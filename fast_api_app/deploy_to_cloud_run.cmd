@REM Deploying to Cloud Run
@pushd ..
@rd /S /Q "%CD%\fast_api_app\CompassUTD" & xcopy "%CD%\CompassUTD" "%CD%\fast_api_app\CompassUTD" /E /I /H /Y
@popd
@gcloud builds submit --config build.yaml
@rd /S /Q "%CD%\fast_api_app\CompassUTD"
@echo Done!