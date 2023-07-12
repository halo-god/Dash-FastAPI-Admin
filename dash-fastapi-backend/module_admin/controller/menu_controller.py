from fastapi import APIRouter, Request
from fastapi import Depends, Header
from config.get_db import get_db
from module_admin.service.login_service import get_current_user
from module_admin.service.menu_service import *
from module_admin.entity.vo.menu_vo import *
from module_admin.dao.menu_dao import *
from utils.response_util import *
from utils.log_util import *
from module_admin.aspect.interface_auth import CheckUserInterfaceAuth
from module_admin.annotation.log_annotation import log_decorator


menuController = APIRouter(dependencies=[Depends(get_current_user)])


@menuController.post("/menu/tree", response_model=MenuTree, dependencies=[Depends(CheckUserInterfaceAuth('common'))])
async def get_system_menu_tree(request: Request, menu_query: MenuTreeModel, query_db: Session = Depends(get_db)):
    try:
        menu_query_result = get_menu_tree_services(query_db, menu_query)
        logger.info('获取成功')
        return response_200(data=menu_query_result, message="获取成功")
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@menuController.post("/menu/forEditOption", response_model=MenuTree, dependencies=[Depends(CheckUserInterfaceAuth('common'))])
async def get_system_menu_tree_for_edit_option(request: Request, menu_query: MenuModel, query_db: Session = Depends(get_db)):
    try:
        menu_query_result = get_menu_tree_for_edit_option_services(query_db, menu_query)
        logger.info('获取成功')
        return response_200(data=menu_query_result, message="获取成功")
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@menuController.post("/menu/get", response_model=MenuResponse, dependencies=[Depends(CheckUserInterfaceAuth('system:menu:list'))])
async def get_system_menu_list(request: Request, menu_query: MenuModel, query_db: Session = Depends(get_db)):
    try:
        menu_query_result = get_menu_list_services(query_db, menu_query)
        logger.info('获取成功')
        return response_200(data=menu_query_result, message="获取成功")
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@menuController.post("/menu/add", response_model=CrudMenuResponse, dependencies=[Depends(CheckUserInterfaceAuth('system:menu:add'))])
@log_decorator(title='菜单管理', business_type=1)
async def add_system_menu(request: Request, add_menu: MenuModel, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        add_menu.create_by = current_user.user.user_name
        add_menu.update_by = current_user.user.user_name
        add_menu_result = add_menu_services(query_db, add_menu)
        logger.info(add_menu_result.message)
        if add_menu_result.is_success:
            return response_200(data=add_menu_result, message=add_menu_result.message)
        else:
            return response_400(data="", message=add_menu_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@menuController.patch("/menu/edit", response_model=CrudMenuResponse, dependencies=[Depends(CheckUserInterfaceAuth('system:menu:edit'))])
@log_decorator(title='菜单管理', business_type=2)
async def edit_system_menu(request: Request, edit_menu: MenuModel, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        edit_menu.update_by = current_user.user.user_name
        edit_menu.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        edit_menu_result = edit_menu_services(query_db, edit_menu)
        if edit_menu_result.is_success:
            logger.info(edit_menu_result.message)
            return response_200(data=edit_menu_result, message=edit_menu_result.message)
        else:
            logger.warning(edit_menu_result.message)
            return response_400(data="", message=edit_menu_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@menuController.post("/menu/delete", response_model=CrudMenuResponse, dependencies=[Depends(CheckUserInterfaceAuth('system:menu:remove'))])
@log_decorator(title='菜单管理', business_type=3)
async def delete_system_menu(request: Request, delete_menu: DeleteMenuModel, query_db: Session = Depends(get_db)):
    try:
        delete_menu_result = delete_menu_services(query_db, delete_menu)
        if delete_menu_result.is_success:
            logger.info(delete_menu_result.message)
            return response_200(data=delete_menu_result, message=delete_menu_result.message)
        else:
            logger.warning(delete_menu_result.message)
            return response_400(data="", message=delete_menu_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@menuController.get("/menu/{menu_id}", response_model=MenuModel, dependencies=[Depends(CheckUserInterfaceAuth('system:menu:edit'))])
async def query_detail_system_menu(request: Request, menu_id: int, query_db: Session = Depends(get_db)):
    try:
        detail_menu_result = detail_menu_services(query_db, menu_id)
        logger.info(f'获取menu_id为{menu_id}的信息成功')
        return response_200(data=detail_menu_result, message='获取成功')
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")
