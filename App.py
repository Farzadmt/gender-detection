{
    "name": "Gender Detection API",
    "description": "An API that detects gender from an uploaded image using DeepFace.",
    "version": "1.0",
    "github_repo": "https://github.com/username/gender-detection",
    "endpoints": [
        {
            "path": "/detect-gender",
            "method": "POST",
            "description": "Upload an image and get gender prediction.",
            "content_type": "multipart/form-data",
            "parameters": [
                {
                    "name": "image",
                    "in": "formData",
                    "required": true,
                    "type": "file",
                    "description": "Image file containing a human face."
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful gender prediction",
                    "content": {
                        "application/json": {
                            "example": {
                                "status": "success",
                                "gender": "Woman",
                                "raw_data": [
                                    {
                                        "dominant_gender": "Woman",
                                        "gender": {
                                            "Woman": 98.7,
                                            "Man": 1.3
                                        }
                                    }
                                ]
                            }
                        }
                    }
                },
                "400": {
                    "description": "Bad request (e.g. no image provided)",
                    "content": {
                        "application/json": {
                            "example": {
                                "status": "error",
                                "message": "No image provided"
                            }
                        }
                    }
                },
                "500": {
                    "description": "Internal server error",
                    "content": {
                        "application/json": {
                            "example": {
                                "status": "error",
                                "message": "Face not detected"
                            }
                        }
                    }
                }
            }
        }
    ]
}
