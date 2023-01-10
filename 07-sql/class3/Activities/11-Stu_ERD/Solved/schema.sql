-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Customer" (
    "customer_id" INT   NOT NULL,
    "first_name" VARCHAR(255)   NOT NULL,
    "last_name" VARCHAR(255)   NOT NULL,
    "gender" VARCHAR(255)   NOT NULL,
    "age" INT   NOT NULL,
    "address" VARCHAR(255)   NOT NULL,
    "city" VARCHAR(255)   NOT NULL,
    "state" VARCHAR(255)   NOT NULL,
    "zip_code" INT   NOT NULL,
    CONSTRAINT "pk_Customer" PRIMARY KEY (
        "customer_id"
     )
);

CREATE TABLE "Banks" (
    "bank_id" INT   NOT NULL,
    "bank_name" VARCHAR(255)   NOT NULL,
    "bank_routing_number" BIGINT   NOT NULL,
    CONSTRAINT "pk_Banks" PRIMARY KEY (
        "bank_routing_number"
     )
);

CREATE TABLE "Sales" (
    "sales_id" INT   NOT NULL,
    "payment_id" INT   NOT NULL,
    "mortgage_id" INT   NOT NULL,
    "loan_amount" INT   NOT NULL,
    "loan_date" DATE   NOT NULL,
    CONSTRAINT "pk_Sales" PRIMARY KEY (
        "sales_id"
     )
);

CREATE TABLE "Payments" (
    "payment_id" INT   NOT NULL,
    "bank_number" BIGINT   NOT NULL,
    "bank_routing_number" BIGINT   NOT NULL,
    "customer_id" INT   NOT NULL,
    CONSTRAINT "pk_Payments" PRIMARY KEY (
        "payment_id"
     )
);

CREATE TABLE "Mortgage" (
    "mortgage_id" INT   NOT NULL,
    "mortgage_name" VARCHAR(255)   NOT NULL,
    "mortgage_rate" FLOAT   NOT NULL,
    CONSTRAINT "pk_Mortgage" PRIMARY KEY (
        "mortgage_id"
     )
);

ALTER TABLE "Sales" ADD CONSTRAINT "fk_Sales_payment_id" FOREIGN KEY("payment_id")
REFERENCES "Payments" ("payment_id");

ALTER TABLE "Sales" ADD CONSTRAINT "fk_Sales_mortgage_id" FOREIGN KEY("mortgage_id")
REFERENCES "Mortgage" ("mortgage_id");

ALTER TABLE "Payments" ADD CONSTRAINT "fk_Payments_bank_routing_number" FOREIGN KEY("bank_routing_number")
REFERENCES "Banks" ("bank_routing_number");

ALTER TABLE "Payments" ADD CONSTRAINT "fk_Payments_customer_id" FOREIGN KEY("customer_id")
REFERENCES "Customer" ("customer_id");

