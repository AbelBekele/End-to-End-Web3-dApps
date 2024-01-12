CREATE TABLE "trainee" (
    "id" SERIAL PRIMARY KEY,
    "trainee" VARCHAR(50) DEFAULT NULL,
    "email" VARCHAR(50),
    "asset" INTEGER,
    "status" VARCHAR(10),
    "remark" VARCHAR(150),
    "hashed" VARCHAR(350) DEFAULT NULL
)