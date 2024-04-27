SELECT C.CAR_ID as CAR_ID, C.CAR_TYPE as CAR_TYPE, ROUND(C.DAILY_FEE * (100-P.DISCOUNT_RATE)/100 * 30) AS FEE 
FROM CAR_RENTAL_COMPANY_CAR C
        JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE
WHERE 
    C.CAR_ID NOT IN ( 
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-12-01'
    ) 
    AND 
    P.DURATION_TYPE like '30%'
GROUP BY C.CAR_ID
HAVING C.CAR_TYPE IN ('세단', 'SUV')
    AND (FEE >= 500000 AND FEE < 2000000)
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC