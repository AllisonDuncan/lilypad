// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table users {
  id integer [primary key]
  user_name varchar
  first_name varchar
  last_name varchar
  role varchar
  bank integer
  cart integer
  chores integer
  created_at timestamp
}

Table bank {
  account_number integer [primary key]
  balance integer
  transaction_history transactions
}

Table transaction {
  transaction_id integer [primary key]
  amount integer
  request_time datetime
  request_type request_type
  status transaction_status
  account_number account_number
}

Enum request_type {
  add
  subtract
}

Enum transaction_status {
  processing
  complete
}

Table product {
  id integer [primary key]
  name varchar
  description varchar
  cost integer //original inventory cost of item
  display_price integer //current cost of item
  link varchar
  image_url varchar
  available_for_sale bool
  cart integer
}

Table cart {
  id integer [primary key]
  name varchar
  // products product // duplication of data unless accelerators needed
}

Table chore {
  id integer [primary key]
  name varchar
  description varchar
  why varchar
  due_date date
  completion_date date
  status chore_status
  required bool
  claimed bool
  claimed_by chore_list
  created_date datetime
  stars integer
}

Table chore_list {
  id integer [primary key]
  name varchar //default User's Chores
  // chores chore // duplication of data unless accelerators needed
}

Enum chore_status {
  available
  claimed
  in_progress
  done
}

Table order {
  order_id integer [primary key]
  user user
  products_in_order products
  total integer
  order_created datetime
}

Ref: cart.id > product.cart

Ref: "users"."bank" - "bank"."account_number"

Ref: "users"."cart" - "cart"."id"

Ref: "chore_list"."id" < "chore"."claimed_by"

Ref: "bank"."transaction_history" < "transaction"."transaction_id"

Ref: "users"."chores" - "chore_list"."id"

Ref: "order"."products_in_order" < "product"."id"