-- SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მხოლოდ customerName, phone, city, country ველებს.
SELECT customerName, phone, city, country FROM customers;
-- SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ყველა იმ ჩანაწერს რომლის ფოსტის კოდი მეტია 1370ზე ან salesRepEmployeeNumber მეტია 150
SELECT * FROM customers WHERE postalCode > 1370 OR salesRepEmployeeNumber > 150;
-- SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ისეთ ჩანაწერს, რომელშიც customerName შეიცავს 'Mini' ტექსტს
SELECT * FROM customers WHERE customerName LIKE '%Mini%';
-- SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონაცემებს, რომელსაც აქვს state 'CA' ან 'NY'
SELECT * FROM customers WHERE state IN ('CA', 'NY');
-- SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონცემებს, რომელსაც აქვს creditLimit 10000-ზე მეტი 
SELECT * FROM customers WHERE creditLimit > 10000;