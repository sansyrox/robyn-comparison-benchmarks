use actix_web::{get, web, App, HttpServer, Responder};

#[get("/")]
async fn greet(name: web::Path<String>) -> impl Responder {
    format!("Hello world!")
}

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(greet))
        .workers(48)
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
